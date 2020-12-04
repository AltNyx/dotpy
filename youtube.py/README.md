# download-youtube-songs

Download songs/audio from youtube videos effortlessly.

## Help

```
usage: python youtube.py [-h] [--audio: bool] [--path: str] video_name

Download youtube songs/videos

positional arguments:
  vid_name       name of the youtube video.

optional arguments:
  -h, --help     show this help message and exit
  --audio AUDIO  Set audio to True to download only audio default: False
  --path PATH    Path where file has to be downloaded, default: current directory
```

## Usage

To download audio only  
`python youtube.py --audio=True --path='path to download folder' <video_name>`

To download video (skip the optional argument --audio)  
`python youtube.py --path='path to download folder <video_name>`

Note: You can skip the --path argument. It will download in the directory from which the program was run.

## Example

`python youtube.py --audio=True --path='./Downloads' 'duumu shifted'`

## Output

```
Video Details:
Title - [Duumu - Shifted]
Views - 33935
Duration - 00:04:29
Downloading...
  4,276,675.0 Bytes [100.00%] received. Rate: [2152 KB/s].  ETA: [0 secs]
```
