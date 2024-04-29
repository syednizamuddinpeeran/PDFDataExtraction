from OpenSource import PyPDF2Loader,PyMuPdfLoader
from pdf import  pdf
from enum import Enum

class PDF_READERS(Enum):
    PyPdf2 = 1,
    Fitz =2,
    PyMuPDF =2
def Load(reader:PDF_READERS,filePath:str)->pdf:
    if reader==PDF_READERS.PyPdf2:
        return PyPDF2Loader(filePath)
    elif reader == PDF_READERS.Fitz or  reader == PDF_READERS.PyMuPDF:
        return PyMuPdfLoader(filePath)