from urllib.request import urlopen
from pathlib import Path
import argparse
import pafy
import sys
import re
import os


class Youtube:
    quality = {'1080p60': 299, '1080p': 137, '720p60': 298, '720p': 136, '480p': 135, '360p': 134}
    def __init__(self, vid_name: str):
        '''
        Parameters:
            vid_name: name of the youtube video
        '''
        self.vid_name = vid_name
    
    @property
    def vid_url(self) -> str:
        '''Get youtube video url from video name'''
        vid_name = '+'.join(self.vid_name.split()).encode('utf-8')
        search_url = f"https://www.youtube.com/results?search_query={vid_name}"
        try:
            html = urlopen(search_url).read().decode()
            video_ids = re.findall(r"watch\?v=(\S{11})", html)
            if video_ids:
                return f"https://www.youtube.com/watch?v={video_ids[0]}"
        except Exception as e:
            print(e)
    
    def video_details(self, video: 'pafy object') -> None:
        '''Prints the video details
        
        Parameters:
            video: pafy video object
        '''
        print("Video Details:")
        print(f"Title - [{video.title}]")
        print(f"Views - {video.viewcount}")
        print(f"Duration - {video.duration}")
        print("Downloading...")
    
    def download_audio(self, url: str, path: str) -> None:
        '''Downloads the best audio from the given youtube video url'''
        print(path)
        video = pafy.new(url)
        self.video_details(video)
        bestaudio = video.getbestaudio(preftype="m4a")
        bestaudio.download(path)
    
    def download_video(self, url: str, path: str) -> None:
        '''downloads the video from the given youtube video url'''
        for quality, itag in Youtube.quality.items():
            status = os.system(f'you-get -o {path} --itag={itag} {url}')
            if status != 0:
                print(f'Could not find {quality} video. Trying lower')
                continue
                
            return
        
        print(f"Coudn't find a decent quality for {url}")


def main():
    parser = argparse.ArgumentParser(
        description='Download youtube songs/videos',
        usage='python youtube.py [-h] [--audio: bool] [--path: str] video_name'
    )

    parser.add_argument(
        'vid_name', 
        type=str, 
        help='name of the youtube video.'
    )

    parser.add_argument(
        '--audio', 
        type=bool, 
        default=False, 
        help='Set audio to True to download only audio default: False'
    )

    parser.add_argument(
        '--path', 
        type=str, 
        default=os.getcwd(), 
        help='Path where file has to be downloaded, default: current directory'
    )

    args = parser.parse_args()
    vid_name, isaudio, path = args.vid_name, args.audio, args.path
    yt = Youtube(vid_name)
    url = yt.vid_url
    yt.download_audio(url, path) if isaudio else yt.download_video(url, path)


if __name__ == "__main__":
    main()