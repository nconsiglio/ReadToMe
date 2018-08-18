from gtts import gTTS
import os
from tkinter import *
import PyPDF2
from pygame import mixer

pdf_file = open('test.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
textTo_read = page_content.encode('utf-8')


language='en'
myob=gTTS(text=page_content,lang=language,slow=False)
myob.save('Voice1.mp3')



mixer.init()
mixer.music.load("Voice1.mp3")
mixer.music.play()
   


