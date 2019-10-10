import csv
import Post

class Csv_failik():
	"""Этот класс будет работать с файлом csv"""

	def read_csv(self, file_name):

		data = []
		one_offer = []

		with open(file_name, 'r', encoding='cp1251', newline='') as f:
			reader = csv.reader(f, delimiter=';')
			for row in reader:
				
				one_offer = [row[0], row[1], row[2], row[3], row[4]]

				data.append(one_offer)

		return data

	def write_csv(self, file_name, data):
		with open(file_name, 'a', encoding='cp1251', newline='') as f:
			writer = csv.writer(f, delimiter=';')
			for offer in data:
				writer.writerow(offer)

	def create_csv(self, file_name):
		data = []
		with open(file_name, 'w', encoding='cp1251', newline='') as f:
			writer = csv.writer(f, delimiter=';')
			for offer in data:
				writer.writerow(offer)

	def fill_posts(self, file_name):
		data = []

		with open(file_name, 'r', encoding='cp1251', newline='') as f:
			reader = csv.reader(f, delimite=';')
			for row in reader:
				price_i = row[1].replace('грн.', '').replace(' ', '')
				try:
					price_i = int(price)
				except:
					price_i = 0
				one_post = Post.Post(name = row[0], price = price_i, city = row[2], date = row[3], url = row[4])
				data.append(one_post)

		return data

