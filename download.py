import pytube
from tkinter import *
from pytube import YouTube
from tkinter import messagebox

window = Tk()
window.title("tubemaker")
window.geometry("500x500")
window.configure()


def click():
	
    inp = input.get()
    yt = YouTube(inp)
    stream = yt.streams.first()
    stream.download()
    global window
    window.destroy()



input = Entry(window)
input.pack()

l1 = Label(window, text="URL", fg="black", font="none 12 bold")
l1.pack()

b1 = Button(window, text="Press the button to begin downloading your video",
width=70, command=click)
b1.pack()

window.mainloop()


    # https://www.youtube.com/watch?v=9uDgJ9_H0gg