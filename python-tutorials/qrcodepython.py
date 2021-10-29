# ==== Criando QR Code com Python ===== #

import pyqrcode
import png

site = "https://github.com/patrulha-fiap"

#pyqrcode.create recebe o site que sera encaminhado pelo QR code
url = pyqrcode.create(site)

#url.png recebe o nome do arquivo e o scale da imagem
url.png("qr_patrulha.png", scale=5)