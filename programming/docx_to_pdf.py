#pip install docx2pdf
from docx2pdf import convert

# Documento para ser convertido, novo documento
convert("documento.docx", "documento.pdf")
