from tkinter import *

window = Tk()
window.title("Instagram Profile Downloader")
window.geometry("500x500")
Label(window, text="Enter your instagram username").pack()
username = Entry(window, width=30)
username.pack()
button = Button(window, width=20, text="Start downloading...")
button.pack()
label = Label(window)
window.mainloop()