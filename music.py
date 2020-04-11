import os
from tkinter.filedialog import askdirectory
 
import pygame
from mutagen.id3 import ID3
from tkinter import *
 
root = Tk()
root.minsize(100,100)
 
 
listofsongs = []
realnames = []
 
v = StringVar()
songlabel = Label(root,textvariable=v,width=50)
 
index = 0
 
def directorychooser():
 
    directory = askdirectory()
    os.chdir(directory)
 
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
 
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            if 'TIT2' in audio:
                realnames.append(audio['TIT2'].text[0])
 
 
            listofsongs.append(files)
 
 
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
 
directorychooser()
 
def updatelabel():
    global index
    global songname
    v.set(realnames[index])
 
 
 
def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
 
def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
 
 
def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
 
 
label = Label(root,text='Music Player')
label.pack()
 
listbox = Listbox(root,width=50)
listbox.pack()
realnames.reverse()
 
for items in realnames:
    listbox.insert(0,items)
 
realnames.reverse()
 
 
nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()
 
previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()
 
stopbutton = Button(root,text='Stop Music')
stopbutton.pack()
 
 
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
 
songlabel.pack()
 
root.mainloop()
