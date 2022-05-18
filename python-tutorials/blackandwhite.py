from PIL import Image

img = Image.open("buzz.png")
pretoebranco =  img.convert("L")
pretoebranco.save("pretoebrancobuzz.png")
pretoebranco.show()