from pytube import YouTube


url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

yt = YouTube(url)

print(f'Title: {yt.title}')
print(f'Number of views: {yt.views}')
print(f'Length of video: {yt.length} seconds')

stream = yt.streams.get_highest_resolution()
stream.download()

print('Video muvaffaqiyatli yuklandi!')
