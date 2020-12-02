import pafy
import pytube
from convert import convert_duration, convert_likes, convert_views, convert_title, convert_channel


def vid_details(url):
    vid = pafy.new(url)
    details = {}
    details['Title'] = convert_title(vid.title)
    details['Channel'] = convert_channel(vid.author)
    details['Views'] = convert_views(vid.viewcount)
    details['Likes'] = convert_likes(vid.likes)
    details['Duration'] = convert_duration(vid.duration)
    return details


def vid_streams(url):
    vid = pafy.new(url)
    choices = {}
    streams = vid.allstreams
    for stream in streams:
        if str(stream.mediatype) == 'video':
            continue
        media = str(stream.mediatype)
        res = str(stream.quality)
        ext = str(stream.extension)
        size = stream.get_filesize()/1024**2
        size = "%.2f" % size
        choice = f"[{media}][{res}][{ext}][{size}MB]"
        choices[choice] = stream
    return choices


def dwnld_vid(url, req, path):
    choices = vid_streams(url)
    choice = choices[req]
    choice.download(path)
