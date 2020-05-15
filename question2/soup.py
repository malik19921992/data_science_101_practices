#!/usr/bin/env python3

from PyDictionary import PyDictionary
import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import pandas as pd
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from fpdf import FPDF 


WORD = "soup"
url = f'https://en.wikipedia.org/wiki/{WORD}'


def dictionary_searching(WORD):
	global dictionary
	dictionary=PyDictionary()
	print(dictionary.meaning(WORD)["Noun"][0] , end ='')
	for find in dictionary.meaning(WORD)["Noun"][1:]:
		print(f' - {find}',end='')



def most_common_data_scrapping(url,num):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml")
	text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
	c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
	data = c.most_common()[:num]
	data2 = {}
	data2["names"] = []
	data2["numbers"] = []
	num = 0
	for i in data:
		data2["names"].append(f'{i[0]}:')
		data2["numbers"].append(i[1])
		num = num + 1
	df = pd.DataFrame(data2)
	print(df.to_string(index=False,header=False))

def pdf_space_line(num):
	pdf.set_font("Arial",style='I' ,size = 10)
	for i in range(num):
		pdf.cell(0, 1 , txt = f"             ",ln = 1, align = 'E')

def save_pdf():
	dictionary=PyDictionary()
	global pdf
	pdf = FPDF() 
	pdf.add_page() 
	
	pdf.set_font("Arial",'B' ,size = 27) 
	pdf.cell(0, 10, txt = "     SOUP",ln = 1, align = 'E') 
	
	pdf.image('soup_image.jpg',25,22,160)
	
	pdf.set_font("Arial",style='I' ,size = 10)
	pdf_space_line(90)
	pdf.cell(0, 1 , txt = f"              {url}",ln = 3, align = 'E')
	
	pdf_space_line(8)
	pdf.cell(14)
	pdf.set_font("Arial",style='B' ,size = 14)
	pdf.cell(0, 1 , txt = f"NOUN",ln = 3, align = 'E')
	
	pdf_space_line(8)
	pdf.set_font("Arial",size = 10)
	
	for find in dictionary.meaning(WORD)["Noun"]:
		pdf.cell(14)
		pdf.cell(0, 1 , txt = f"- {find}",ln = 3, align = 'E')
		pdf_space_line(3)

	pdf_space_line(8)
	pdf.cell(14)
	pdf.set_font("Arial",style='B' ,size = 14)
	pdf.cell(0, 1 , txt = f"VERB",ln = 3, align = 'E')

	pdf_space_line(8)
	pdf.cell(14)
	pdf.set_font("Arial" ,size = 10)
	pdf.cell(0, 1 , txt = f"- {dictionary.meaning(WORD)['Verb'][0]}",ln = 3, align = 'E')

	pdf.output("soup.pdf")



def save_image(url,image_resolution):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml")
	text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
	c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
	data = c.most_common()[:100]
	names = []
	numbers = []
	num = 0
	for i in data:
		names.append(i[0])
		numbers.append(i[1])
	words = pd.Series(index=names, data=numbers)
	wordcloud = WordCloud(max_font_size=75)
	wordcloud.generate_from_frequencies(words)
	plt.figure(figsize = (12,9))
	plt.axis("off")
	fig = plt.imshow(wordcloud,interpolation='nearest')
	fig.axes.get_xaxis().set_visible(False)
	fig.axes.get_yaxis().set_visible(False)
	plt.savefig('soup_image.jpg',bbox_inches='tight', pad_inches=0, format='jpg', dpi=image_resolution)    


if __name__ == '__main__':
	dictionary_searching(WORD)
	print(f'\nWIKIPEDIA {url}')
	most_common_data_scrapping(url,5)
	save_image(url,1200)
	save_pdf()
