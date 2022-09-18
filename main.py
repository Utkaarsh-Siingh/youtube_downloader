import sys, subprocess
from functions import *

if sys.platform == 'linux':
    subprocess.run("clear", shell=True)
elif sys.platform == 'win32':
    subprocess.run('cls', shell=True)

spacer = " " * 20
print("==========YOUTUBE DOWNLOADER==========")
print("\n(1) Video               (2) Video {audio only}")
print("(3) Playlist            (4) Playlist {audio only}")
cho = input("\nEnter Your Choice : ")

if cho == "1":
    link = input("Enter Youtube Link : ")
    video_download(link)

elif cho == "2":
    link = input("Enter Youtube Link : ")
    audio_download(link)

elif cho == '3':
    link = input("Enter Playlist Link : ")
    playlist_download(link)

elif cho == '4':
    link = input("Enter Playlist Link : ")
    playlist_audio_download(link)

else:
    print("Choice Not Exists !")

print("\n==========EXITING==========")