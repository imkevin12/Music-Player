def slider():
    global count, sliderWords
    text = 'Welcome to KEVIN MUSIC PLAYER'
    if (count >= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    slider_label.configure(text=sliderWords)
    slider_label.after(200, slider)

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    progressbarVolume_label.grid()
    root.mute_button.grid()
    progressbarMusic_label.grid()
    mixer.music.set_volume(0.4)
    progressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    audioStatus_label.configure(text='PLAYING')

    Song = MP3(ad)
    totalsonglength = int(Song.info.length)
    progressbarMusic['maximum'] = totalsonglength
    endtimePM_label.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))

    def Progresbarmusictick():
        CurrenSongLength = mixer.music.get_pos() // 1000
        progressbarMusic['value'] = CurrenSongLength
        starttimePM_label.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrenSongLength))))
        progressbarMusic.after(2, Progresbarmusictick)

    Progresbarmusictick()


def pausemusic():
    mixer.music.pause()
    root.pause_button.grid_remove()
    root.resume_button.grid()
    audioStatus_label.configure(text='PAUSED')


def resumemusic():
    root.resume_button.grid_remove()
    root.pause_button.grid()
    mixer.music.unpause()
    audioStatus_label.configure(text='PLAYING')


def stopmusic():
    mixer.music.stop()
    audioStatus_label.configure(text='STOPPED')


def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol + 0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    progressbarVolume['value'] = mixer.music.get_volume() * 100


def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    progressbarVolume['value'] = mixer.music.get_volume() * 100


def mutemusic():
    global currentvol
    root.mute_button.grid_remove()
    root.unmute_button.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)


def unmutemusic():
    global currentvol
    root.unmute_button.grid_remove()
    root.mute_button.grid()
    mixer.music.set_volume(currentvol)


def musicFile_dialog():
    try:
        audioDir = filedialog.askopenfilename(initialdir='C:/Users/dell/Desktop',
                                              title='Select Audio File',
                                              filetype=(('MP3', '*.mp3'), ('WAV', '*.wav')))
    except:
        audioDir = filedialog.askopenfilename(title='Select Audio File',
                                              filetype=(('MP3', '*.mp3'), ('WAV', '*.wav')))
    audiotrack.set(audioDir)
    audioFile = audioDir.split('/')
    audiotrack1.set(audioFile[-1])


def createwidthes():
    global play_img, pause_img, browse_img, volumeup_img, volumedown_img, stop_img, resume_img, mute_img, unmute_img
    global audioStatus_label, ProgressbarVolumeLabel, progressbarVolume, progressbarVolume_label, progressbarMusic_label, progressbarMusic, endtimePM_label, starttimePM_label

    # *************** Images Register *************** #
    browse_img = PhotoImage(file='browsing.png')
    play_img = PhotoImage(file='play.png')
    pause_img = PhotoImage(file='pause.png')
    resume_img = PhotoImage(file='stop1.png')
    stop_img = PhotoImage(file='stop.png')
    volumeup_img = PhotoImage(file='volume-up.png')
    volumedown_img = PhotoImage(file='volume-down.png')
    mute_img = PhotoImage(file='mute.png')
    unmute_img = PhotoImage(file='muted.png')

    # *************** Change Images Size *************** #
    browse_img = browse_img.subsample(2, 2)
    play_img = play_img.subsample(2, 2)
    pause_img = pause_img.subsample(2, 2)
    resume_img = resume_img.subsample(2, 2)
    stop_img = stop_img.subsample(2, 2)
    volumeup_img = volumeup_img.subsample(2, 2)
    volumedown_img = volumedown_img.subsample(2, 2)
    mute_img = mute_img.subsample(2, 2)
    unmute_img = unmute_img.subsample(2, 2)

    # *************** Audio | Browse *************** #
    browse_audio = Entry(root, font=('open sans', 12, 'bold'), width=18, bg='#D0ECE7', disabledbackground="black",
                         disabledforeground="white", state='disabled', textvariable=audiotrack1)
    browse_audio.grid(row=1, column=0, columnspan=2)

    browse_button = Button(root, text='Browse', font=('futura', 13),bg='#CB4335', activebackground='#CD6155', relief=RAISED, width=90, bd=3, image=browse_img, compound=RIGHT,
                           command=musicFile_dialog)
    browse_button.grid(row=1, column=2)

    # *************** Play | Pause | Resume | Stop *************** #
    play_button = Button(root, text='Play', font=('futura', 13), width=90, bd=3, image=play_img, bg='#52BE80', activebackground='#7DCEA0', relief=RAISED, compound=RIGHT,
                         command=playmusic)
    play_button.grid(row=2, column=0)

    root.pause_button = Button(root, text='Pause', font=('futura', 13), bg='#52BE80', activebackground='#7DCEA0', relief=RAISED, width=90, bd=3, image=pause_img, compound=RIGHT,
                               command=pausemusic)
    root.pause_button.grid(row=2, column=1)

    root.resume_button = Button(root, text='Resume', font=('futura', 13), bg='#52BE80', activebackground='#7DCEA0', relief=RAISED, width=90, bd=3, image=resume_img,
                                compound=RIGHT, command=resumemusic)
    root.resume_button.grid(row=2, column=1)
    root.resume_button.grid_remove()

    stop_button = Button(root, text='Stop', font=('futura', 13), bg='#52BE80', activebackground='#7DCEA0', relief=RAISED, width=90, bd=3, image=stop_img, compound=RIGHT,
                         command=stopmusic)
    stop_button.grid(row=2, column=2)

    # *************** Volume-up | Volume-down | Audio Status *************** #
    volumeUp_Button = Button(root, text='Volume', font=('futura', 13), bg='#5499C7', activebackground='#7FB3D5', relief=RAISED, width=90, bd=3, image=volumeup_img,
                             compound=RIGHT, command=volumeup)
    volumeUp_Button.grid(row=3, column=0)

    audioStatus_label = Label(root, text='', background='black', fg='white', font=('open sans', 12, 'bold'), width=9)
    audioStatus_label.grid(row=3, column=1)

    volumeDown_button = Button(root, text='Volume', font=('futura', 13),bg='#5499C7', activebackground='#7FB3D5', relief=RAISED, width=90, bd=3, image=volumedown_img,
                               compound=RIGHT, command=volumedown)
    volumeDown_button.grid(row=3, column=2)

    # *************** Mute | Unmute *************** #
    root.mute_button = Button(root, width=30, bd=1, relief=SOLID,
                              image=mute_img, compound=RIGHT, command=mutemusic)
    root.mute_button.grid(row=4, column=3)
    root.mute_button.grid_remove()

    root.unmute_button = Button(width=30, bd=1, relief=SOLID,
                                image=unmute_img, compound=RIGHT, command=unmutemusic)
    root.unmute_button.grid(row=4, column=3)
    root.unmute_button.grid_remove()

    # *************** Progressbar Volume *************** #
    progressbarVolume_label = Label(root, text='', bg='red')
    progressbarVolume_label.grid(row=1, column=3, rowspan=3)

    progressbarVolume = Progressbar(progressbarVolume_label, orient=VERTICAL, mode='determinate',
                                    value=0, length=120)
    progressbarVolume.grid(row=1, column=0, ipadx=5)

    ProgressbarVolumeLabel = Label(progressbarVolume_label, text='0%', bg='lightgray', width=3)
    ProgressbarVolumeLabel.grid(row=1, column=0)
    progressbarVolume_label.grid_remove()

    # *************** Progressbar Music *************** #
    progressbarMusic_label = Label(root, text='', bg='red')
    progressbarMusic_label.grid(row=4, column=0, columnspan=3)
    progressbarMusic_label.grid_remove()

    starttimePM_label = Label(progressbarMusic_label, text='0:00:0', bg='red', width=5)
    starttimePM_label.grid(row=0, column=0)

    progressbarMusic = Progressbar(progressbarMusic_label, orient=HORIZONTAL, mode='determinate', value=0)
    progressbarMusic.grid(row=0, column=1, ipadx=56, ipady=3)

    endtimePM_label = Label(progressbarMusic_label, text='0:00:0', bg='red')
    endtimePM_label.grid(row=0, column=2)


# *************** Initially *************** #
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

root = Tk()
root.geometry('338x185+500+150')
root.title('Music Player')
root.iconbitmap('music.ico')
root.resizable(0, 0)

# *************** Gloabl Vraiables *************** #
audiotrack = StringVar()
audiotrack1 = StringVar()
currentvol = 0
totalsonglength = 0
count = 0
text = ''
sliderWords = ''

# *************** Slider *************** #
slider_label = Label(root, text='', font=('Verdana', 12, 'bold'), width=27, bg='black', fg='white', justify=CENTER)
slider_label.grid(row=0, column=0, columnspan=4)
slider()

mixer.init()
createwidthes()
root.mainloop()
