import instaloader
import urllib
import io
from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk


def get_image():
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, f"{username.get()}")
    link = urlopen(profile.get_profile_pic_url())
    data = link.read()
    link.close()
    image = Image.open(io.BytesIO(data))
    picture = ImageTk.PhotoImage(image)
    label.config(image=picture)
    label.image = picture
    label.pack()


window = Tk()
window.title("Instagram Profile Downloader")
window.geometry("500x500")
Label(window, text="Enter your instagram username").pack()
username = Entry(window, width=30)
username.pack()
button = Button(window, width=20, text="Start downloading...")
button.pack()
button.config(command=get_image)
label = Label(window)
window.mainloop()