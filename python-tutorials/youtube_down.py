from pytube import YouTube

link = "https://www.youtube.com/watch?v=NM3HVHvFWRg"

try: 
    yt = YouTube(link)
except:
    print("Erro de conexao")

try:
    #fazendo download do video
    yt.streams.filter(progressive=True, file_extension="mp4").first().download()
except:
    print("Erro ao fazer o download")
print("D")