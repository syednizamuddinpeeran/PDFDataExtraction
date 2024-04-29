from PyPDF2 import PdfReader
import fitz
from pdf import pdf,text,page,image

def PyPDF2Loader(filePath)->pdf:
    pdfObj = pdf(filePath) 
    pdfObj.filePath = filePath
    reader = PdfReader(filePath)
    for p in reader.pages:
        pdfPage = page()
        pdfPage.text = p.extract_text()
        pdfPage.elements.append(text(pdfPage.text))
        for i in p.images:
            pdfPage.elements.append(image(i))
        pdfObj.pages.append(pdfPage)
    return pdfObj

def PyMuPdfLoader(filePath)->pdf:
    pdfObj = pdf(filePath) 
    pdfObj.filePath = filePath
    fitObj = fitz.open(filePath)
    for p in fitObj:
        pdfPage = page()
        pdfPage.text = p.get_text()
        #to implement image extraction
        pdfObj.pages.append(pdfPage)
    return pdfObj