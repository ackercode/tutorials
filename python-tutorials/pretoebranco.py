#Convertendo imagem em preto e branco

from PIL import Image

#instalar pacote -> pip install Pillow

img = Image.open("buzz.png")
blackandwrite = img.convert("L")
blackandwrite.save("bw_buzz.png")
blackandwrite.show()