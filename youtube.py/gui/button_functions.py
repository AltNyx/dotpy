from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from yt import vid_details, vid_streams, dwnld_vid
from urllib.request import urlopen
from thumnail import get_thumbnail


def select_dir():
    path = filedialog.askdirectory()
    var.set(path)


# def get_details():
#     url = url_var.get()
#     if not url:
#         return
#     details = vid_details(url)
#     update(details)
#     val.clear()
#     url = url_var.get()
#     choices = vid_streams(url)
#     print(choices)
#     for stream in choices:
#         val.append(stream)
#     option.configure(values=val)


# def update(details):
#     title.set('Title: ' + details['Title'])
#     channel.set('Channel: ' + details['Channel'])
#     views.set('Views: ' + details['Views'])
#     likes.set('Likes: ' + details['Likes'])
#     duration.set('Duration: ' + details['Duration'])


# def download_file():
#     path = save_box_var
#     print(choice.get())
#     stream = choices[str(choice.get())]
#     dwnld_vid(stream, path)
