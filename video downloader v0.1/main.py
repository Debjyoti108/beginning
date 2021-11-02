from pytube import YouTube

my_video = YouTube("https://www.youtube.com/watch?v=7BXJIjfJCsA&t=160s") #edit this line in the bracket with the video link you want to download

print("***************Video Title*******************")
print(my_video.title)

print("***************Thumbnail*******************")
print(my_video.thumbnail_url)

print("***************Download Video*******************")

my_video = my_video.streams.get_highest_resolution()

my_video.download()
