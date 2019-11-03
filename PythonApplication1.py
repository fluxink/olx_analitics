# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv_failik
from tkinter import *
from tkinter import messagebox as mb

def get_html(url):
	r = requests.get(url)
	return r.text

def get_total_pages(html):
	soup = BeautifulSoup(html, 'lxml')

	try:
		pages = soup.find('div', class_='pager rel clr').find_all('a', class_='block br3 brc8 large tdnone lheight24')[-1].get('href')
	except:
		mb.showerror('Ошибка', 'Количество объявлений на сайте меньше 39')
	total_pages = pages.split('=')[-1]

	print('Всего страниц: ' + total_pages)
	return int(total_pages)

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	data = []

	offers = soup.find('table', class_='fixed offers breakword redesigned').find_all('div', class_='offer-wrapper')

	for offer in offers:
		try:
			title = offer.find('h3').text.strip()
		except:
			title = ''

		try:
			url = offer.find('h3').find('a').get('href')
		except:
			url = ''

		try:
			price = offer.find('p', class_='price').text.strip()
		except:
			price = ''

		try:
			city = offer.find_all('small', class_='breadcrumb x-normal')[1].text.strip()
		except:
			city = ''

		try:
			time = offer.find_all('small', class_='breadcrumb x-normal')[-1].text.strip()
		except:
			time = ''

		#one_offer = [title.replace('\u200e','').replace('\uff0b', '+').replace('\u20bd', '').replace('\xd7', 'x'), 
					#price.replace('\u200e','').replace('\uff0b', '+').replace('\u20bd', ''), 
					#city.replace('\u200e','').replace('\uff0b', '+').replace('\u20bd', ''), 
					#time.replace('\u200e','').replace('\uff0b', '+').replace('\u20bd', ''), 
					#url.replace('\u200e','').replace('\uff0b', '+').replace('\u20bd', '')]

		city_i = city.split(',')

		one_offer = [title.encode('cp1251', 'ignore').decode('cp1251'), 
					price.encode('cp1251', 'ignore').decode('cp1251'), 
					city_i[0].encode('cp1251', 'ignore').decode('cp1251'), 
					time.encode('cp1251', 'ignore').decode('cp1251'), 
					url.encode('cp1251', 'ignore').decode('cp1251')]

		data.append(one_offer)

	print(len(data))
	return (data)

def start(url, file_name, pages):
	
	try:
		usr_pages = int(pages)
	except:
		usr_pages = ''

	page_part = '/?page='
	csv_file = csv_failik.Csv_failik()

	total_pages = get_total_pages(get_html(url))

	try:
		if total_pages < usr_pages:
			gnrl_pages = total_pages

		elif usr_pages < total_pages:
			gnrl_pages = usr_pages

		else:
			gnrl_pages = total_pages
	except:
		gnrl_pages = total_pages

	csv_file.create_csv(file_name)

	print('Будет обработано страниц: ' + str(gnrl_pages))

	for i in range(1, gnrl_pages):
		url_gen = url + page_part + str(i)
		html = get_html(url_gen)		
		csv_file.write_csv(file_name, data=get_page_data(html))