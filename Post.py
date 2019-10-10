
class Post():
	"""Класс объявления"""

	def __init__(self, name, price, city, date, url):
		self.name = name
		self.price = price
		self.city = city
		self.date = date
		self.url = url

	def name():
		return self.name

	def price():
		return self.price

	def city():
		return self.city

	def date():
		return self.date

	def url():
		return self.url

class Post_process():

	def __init__(self, data_p):
		self.data_p = data_p

	def avg_price_in_city(self, city_name, city_count):
		prices = []

		for post in self.data_p:
			if post.city == city_name:
				total = post.price + total
				prices.append(post.price)

		prices.sort()
		min_price = prices[0]
		max_price = prices[-1]
		avg = total / city_count

		result = [avg, min_price, max_price]
		return (result)
