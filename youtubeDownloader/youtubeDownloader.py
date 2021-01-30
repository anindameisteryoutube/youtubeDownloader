import pytube
url="https://www.youtube.com/watch?v=9TlHvipP5yA"
youtube=pytube.YouTube(url)
streams=youtube.streams.all()
for i in streams:
    print(i)
video=youtube.streams.get_by_itag(22)
directory='H:\YoutubeDownloadedVideos\downloadedByPythonProgram'
video.download(directory)
print('done')