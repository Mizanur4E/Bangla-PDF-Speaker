# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:31:05 2020

@author: Nayan
"""

from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from gtts import gTTS
import playsound
import os




pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text=[]


images = convert_from_path('my.pdf',fmt='jpeg', first_page=5, last_page=6)
for image in images:	
	
	image = image.convert('LA')
	threshold = 90
	im = image.point(lambda p: p > threshold and 255)
	im.show()
	t=pytesseract.image_to_string(im, lang='ben') 
	text.append(t)


for page in text:
		
	tts = gTTS(text=page, lang='bn')
	tts.save("gd.mp3")
	os.system("mpg321 gd.mp3")
	playsound.playsound('gd.mp3', True)
	os.remove('gd.mp3')
