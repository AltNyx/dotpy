from matplotlib import pyplot as plt
from matplotlib import ticker
import csv

time, download, upload = [], [], []

with open('monitor.csv', 'r') as csvfile:
    plots = csv.reader(csvfile)
    next(csvfile)  # Skip the header row
    for row in plots:
        time.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))

plt.figure()
plt.plot(time, download, label='download', color='r')
plt.plot(time, upload, label='download', color='b')
plt.title('Internet Speed')
plt.xticks(rotation=360-45)
plt.xlabel('time')
plt.ylabel('speed in Mb/s')
plt.legend()
plt.savefig('speed.jpg', bbox_inches='tight')
