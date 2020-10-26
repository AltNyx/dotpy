import speedtest
import datetime
import time
import csv

s = speedtest.Speedtest()


with open('monitor.csv', 'w', newline='') as csvfile:
    fieldnames = ['time', 'downspeed', 'upspeed']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    while True:
        day = datetime.datetime.now()
        time_ = datetime.datetime.now().strftime("%H:%M")
        downspeed = round(s.download()/1024**2, 2)
        upspeed = round(s.upload()/1024**2, 2)
        writer.writerow(
            {'time': time_, 'downspeed': downspeed, 'upspeed': upspeed})
        time.sleep(60)
