# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv_failik

def get_html(url):
	r = requests.get(url)
	return r.text

def get_total_pages(html):
	soup = BeautifulSoup(html, 'lxml')

	pages = soup.find('div', class_='pager rel clr').find_all('a', class_='block br3 brc8 large tdnone lheight24')[-1].get('href')
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

		one_offer = [title.encode('cp1251', 'ignore').decode('cp1251'), 
					price.encode('cp1251', 'ignore').decode('cp1251'), 
					city.encode('cp1251', 'ignore').decode('cp1251'), 
					time.encode('cp1251', 'ignore').decode('cp1251'), 
					url.encode('cp1251', 'ignore').decode('cp1251')]

		data.append(one_offer)

	print(len(data))
	return (data)

def start(url, file_name):
	page_part = '/?page='
	csv_file = csv_failik.Csv_failik()

	total_pages = get_total_pages(get_html(url))

	csv_file.create_csv(file_name)

	for i in range(1, 3):
		url_gen = url + page_part + str(i)
		html = get_html(url_gen)		
		csv_file.write_csv(file_name, data=get_page_data(html))