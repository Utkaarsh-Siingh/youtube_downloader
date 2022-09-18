from pytube import YouTube, Playlist
import subprocess, urllib.request, os

def net_connection(host = 'https://www.youtube.com'):
    try:
        urllib.request.urlopen(host)
        return True

    except:
        return False

def video_download(url):
    global file_size
    if net_connection() == True:
        yt_video = YouTube(url)
        dir = 'videos'
        if os.path.exists(dir) == False:
            subprocess.run('mkdir ' + dir, shell=True)
        yt_video.streams.get_by_resolution("720p").download(output_path=dir)
        print("Video Downloaded : ", yt_video.title)

    else:
        print("Internet Seems Unavailable !")

def audio_download(url):
    if net_connection() == True:
        yt_audio = YouTube(url)
        dir = 'audios'
        if os.path.exists(dir) == False:
            subprocess.run('mkdir ' + dir, shell=True)
        yt_audio.streams.get_audio_only().download(output_path=dir)
        print("Audio Downloaded : ", yt_audio.title)

    else:
        print("Internet Seems Unavailable !")

def playlist_download(url):
    if net_connection() == True:
        pl_video = Playlist(url)
        dir = "playlist_videos"
        if os.path.exists(dir) == False:
            subprocess.run('mkdir ' + dir, shell=True)
        for videos in pl_video.videos:
            videos.streams.get_by_resolution("720p").download(output_path=dir)
            print("Video Downloaded : ", videos.title)

    else:
        print("Internet Seems Unavailable !")

def playlist_audio_download(url):
    if net_connection() == True:
        pl_audio = Playlist(url)
        dir = "playlist_audios"
        if os.path.exists(dir) == False:
            subprocess.run("mkdir " + dir, shell=True)
        for audios in pl_audio.videos:
            audios.streams.get_audio_only().download(output_path=dir)
            print("Audio Downloaded : ", audios.title)
    
    else:
        print("Internet Seems Unavailable !")