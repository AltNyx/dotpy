from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from yt import vid_details, vid_streams, dwnld_vid
from urllib.request import urlopen
from thumnail import get_thumbnail

WIDTH = 800
HEIGHT = 435

# Quality Choices
choices = {}

# Colors
overlay = "#924343"
body = "#EF7B7B"
txtcol = "#EBBABA"
boxcol = "#F7D7D7"
btncol = "#F29191"
dwnld = "#F36565"

root = Tk()
root.title("Youtube Downloader")
root.geometry("800x435")
root.config(bg=body)
root.maxsize(WIDTH, HEIGHT)

# Right window
right_overlay = Frame(root, width=477, height=424, bg=overlay)
right_overlay.place(x=318, y=5)

# Left window
left_overlay = Frame(root, width=308, height=243, bg=overlay)
left_overlay.place(x=5, y=186)

# Thumbnail image
size = 308, 171
load = Image.open("maxresdefault.jpg")
load.thumbnail(size)
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=5, y=5)

# Functions


def select_dir():
    path = filedialog.askdirectory()
    save_box_var.set(path)


def get_details():
    url = url_var.get()
    if not url:
        return
    details = vid_details(url)
    update(details)
    val.clear()
    url = url_var.get()
    choices = vid_streams(url)
    print(choices)
    for stream in choices:
        val.append(stream)
    option.configure(values=val)


def update(details):
    title.set('Title: ' + details['Title'])
    channel.set('Channel: ' + details['Channel'])
    views.set('Views: ' + details['Views'])
    likes.set('Likes: ' + details['Likes'])
    duration.set('Duration: ' + details['Duration'])


def download_file():
    path = save_box_var
    print(choice.get())
    stream = choices[str(choice.get())]
    dwnld_vid(stream, path)


# App Name
ttk.Label(root, text="Youtube Downloader",
          font=("roboto condensed", 30, "bold", "underline"), background=overlay, foreground=txtcol).place(x=390, y=10)

# Url box
url_var = StringVar()
ttk.Entry(right_overlay, textvariable=url_var).place(
    width=355, height=29, x=106, y=94)
ttk.Label(right_overlay, text="Url", font=("roboto condensed", 20,
                                           "bold"), background=overlay, foreground=txtcol).place(x=11, y=90)

# Quality box
val = []
choice = StringVar()
option = ttk.Combobox(right_overlay, textvariable=choice, values=val)
option.place(width=355, height=29, x=106, y=160)
ttk.Label(right_overlay, text="Quality", font=("roboto condensed", 20,
                                               "bold"), background=overlay, foreground=txtcol).place(x=11, y=155)

# Save to box
save_box_var = StringVar()
savebox = ttk.Entry(right_overlay, textvariable=save_box_var).place(
    width=355, height=29, x=106, y=226)
ttk.Label(right_overlay, text="Save to", font=("roboto condensed", 20,
                                               "bold"), background=overlay, foreground=txtcol).place(x=11, y=221)


# Buttons
# Search button
search = Button(right_overlay, text="Search", bg=btncol,
                fg="white", font=("roboto condensed", 14, "bold"), relief=GROOVE, command=get_details)
search.place(width=96, height=24, x=362.5, y=97)


# Browse button
browse = Button(right_overlay, text="Browse", bg=btncol, fg="white",
                font=("roboto condensed", 14, "bold"), relief=GROOVE, command=select_dir)
browse.place(width=96, height=24, x=362.5, y=229)

# Download button
download = Button(right_overlay, text="Download", bg=dwnld,
                  fg="white", font=("roboto condensed", 20, "bold"), relief=GROOVE, command=download_file)
download.place(width=149, height=37, x=145, y=299)

# Status box


# Video details
# Title
title = StringVar()
ttk.Label(left_overlay, textvariable=title, background=overlay,
          foreground=txtcol, font=("roboto condensed", 17, "bold"), width=25).place(x=7, y=35)

# Channel
channel = StringVar()
ttk.Label(left_overlay, textvariable=channel, background=overlay,
          foreground=txtcol, font=("roboto condensed", 17, "bold")).place(x=7, y=75)

# Views
views = StringVar()
ttk.Label(left_overlay, textvariable=views, background=overlay,
          foreground=txtcol, font=("roboto condensed", 17, "bold")).place(x=7, y=115)

# Likes
likes = StringVar()
ttk.Label(left_overlay, textvariable=likes, background=overlay,
          foreground=txtcol, font=("roboto condensed", 17, "bold")).place(x=7, y=155)

# Duration
duration = StringVar()
ttk.Label(left_overlay, textvariable=duration, background=overlay,
          foreground=txtcol, font=("roboto condensed", 17, "bold")).place(x=7, y=195)


root.mainloop()
