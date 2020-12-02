from pytube import YouTube


def get_thumbnail(url):
    yt = YouTube(url)
    return yt.thumbnail_url
