from pathlib import Path
import pafy
import sys

# path where the songs are downloaded
# change path as per your wish
PATH = Path("C:\\Users\\ctrla\\Downloads\\music")


# printing video details
def video_details(video):
    print("Video Details:")
    print(f"Title - [{video.title}]")
    print(f"Views - {video.viewcount}")
    print(f"Duration - {video.duration}")
    print("Downloading...")


# downloads the best audio from the given video url
def download(video):
    bestaudio = video.getbestaudio()
    bestaudio.download(PATH)


def main():
    url = sys.argv[1]
    try:
        video = pafy.new(url)
        video_details(video)
        download(video)
    except Exception as e:
        print("Video could not be downloaded!")


if __name__ == "__main__":
    main()
