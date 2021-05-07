# Antes de mais nada -> pip install pypdf2

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

def password_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))

    parser.encrypt(password)
    with open(f"pdf_senha_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"pdf_senha_{file} Criado")

if __name__ == "__main__":
    file = sys.argv[1]
    password = sys.argv[2]
    password_pdf(file, password)

# Primeiro chamamos a funcao que voce criou depois o nome do pdf depois a senha que voce quer colocar
# Chamando no terminal python3 pdfpassword.py teste.pdf 123456