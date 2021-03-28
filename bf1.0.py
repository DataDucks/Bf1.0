# import
import tkinter as tk
from tkinter import simpledialog
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import lxml
import cchardet
from sys import exit
import time
import requests

master = tk.Tk()
master.withdraw()
try:
	# the input dialog
	word = simpledialog.askstring(title="?",
	                                  prompt="WaTCHU nEED?")

	print(' ')
	try:
		wordCapitalize = word.capitalize()
	except AttributeError:
		print ('Enter a word, dummy.')
		exit()
	print ('Word:',wordCapitalize)

	try:
		contentD = urllib.request.urlopen('https://www.dictionary.com/browse/{0}'.format(word))
		read_contentD = contentD.read()
		soupD = BeautifulSoup(read_contentD,'lxml')
	except urllib.error.HTTPError:
		print('urllib.error.HTTPError: That word does not exist')
		exit()

	print(' ')
	span = soupD.find('span', {'class' : 'one-click-content css-ibc84h e1q3nk1v1'})
	print('Definition:',span.text)

	contentP = "https://sentencedict.com/{0}.html".format(word)
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = Request(contentP,headers=hdr)
	read_contentP = urlopen(req)





	try:
		soupP = BeautifulSoup(read_contentP,'lxml')
		p = soupP.find('div', {'id' : 'all'}).find_all('div', {'id' : ''}, limit=31)
		print(' ')
		try:
			x = 0
			maximum_length = 30
			minimum_length = 5
			character_length = len(p[x].text.replace(" ", ""))
		
			while character_length > maximum_length:	
				x += 1
				character_length = len(p[x].text.replace(" ", ""))
			while character_length < minimum_length:
				x += 1
				character_length = len(p[x].text.replace(" ", ""))

			po = p[x].text #paragraph original
			pr = po[2:] #paragraph remove first 3 characters (1. )
			print('Sentence:',pr)
			print(character_length)
		except IndexError:
			x = 0
			maximum_length = 50
			minimum_length = 5
			character_length = len(p[x].text.replace(" ", ""))
		
			while character_length > maximum_length:	
				x += 1
				character_length = len(p[x].text.replace(" ", ""))
			while character_length < minimum_length:
				x += 1
				character_length = len(p[x].text.replace(" ", ""))

			po = p[x].text #paragraph original
			pr = po[2:] #paragraph remove first 3 characters (1. )
			print('Sentence:',pr)
			print(character_length)
		except:
			contentP = urllib.request.urlopen('https://searchsentences.com/words/{0}-in-a-sentence'.format(word))
			read_contentP = contentP.read()
			soupP = BeautifulSoup(read_contentP,'lxml')
			p = soupP.find('div', {'class' : 'row'}).find_next('div', {'class' : 'row'}).find_next('div', {'class' : 'row'}).find_next('div', {'class' : 'row'}).find('div', {'class' : 'col-8'}).find('ul').find('li', {'class' : 'sentence-row'}).find('span')
			print('Sentence:',p.text)
	except:
		print('its broken')

	contentS = urllib.request.urlopen('https://www.wordhippo.com/what-is/another-word-for/{0}.html'.format(word))
	read_contentS = contentS.read()
	soupS = BeautifulSoup(read_contentS,'lxml')

	print(' ')
	try:
		divS = soupS.find_all('div', {'class' : 'wb'}, limit=6)
		print('Synonym:',divS[0].text)
		print('        ',divS[1].text)
		print('        ',divS[2].text)
		print('        ',divS[3].text)
		print('        ',divS[4].text)
	except IndexError:
		print("IndexError: Cannot find all synonyms")

	contentA = urllib.request.urlopen('https://www.wordhippo.com/what-is/the-opposite-of/{0}.html'.format(word))
	read_contentA = contentA.read()
	soupA = BeautifulSoup(read_contentA,'lxml')

	print(' ')
	try:
		divA = soupA.find_all('div', {'class' : 'wb'}, limit=6)
		print('Antonym:',divA[0].text)
		print('        ',divA[1].text)
		print('        ',divA[2].text)
		print('        ',divA[3].text)
		print('        ',divA[4].text)
	except IndexError:
		print("IndexError: Cannot find all antonyms")

	exit()
except KeyboardInterrupt:
	print('Bye')