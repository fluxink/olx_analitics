from itertools import groupby
from collections import Counter
import Post

def avg_price_total(data):
        prices = []
        total = 0
        for i in range(0, len(data)):
                prc = data[i][1].replace('грн.', '').replace(' ', '')
                try:
                        prices.append(int(prc))
                except:
                        prices.append(0)

        for i in range(0, len(data)):
                total = total + prices[i]

        avg_price = total / len(data)
        prices.sort()
        min_price = prices[0]
        max_price = prices[-1]

        result = [round(avg_price), min_price, max_price]
        return (result)

def cities(data):
    data_cities = []

    for i in range (0, len(data)):
        data_cities.append(data[i][2])

    data_cities.sort()
    new_cities = [el for el, _ in groupby(data_cities)]

    return (new_cities)

def numder_of_offers_by_cities(data):
    data_cities = []

    for i in range (0, len(data)):
        data_cities.append(data[i][2])

    dic_of_offers = Counter(data_cities)

    return(dic_of_offers)

def time_of_offers(data):
    data_time = []

    for i in data:
        time = i[3]
        chk_time = time.split(' ')

        if chk_time[0] == 'Сегодня' or chk_time[0] == 'Вчера':
            time = chk_time[0]
        
        data_time.append(time)

    dic_time = Counter(data_time)

    return dic_time

def time_list(data):
    data_time = []
     
    for i in data:
        time = i[3]
        chk_time = time.split(' ')

        if chk_time[0] == 'Сегодня' or chk_time[0] == 'Вчера':
            time = chk_time[0]

        data_time.append(time)

    new_time = [el for el, _ in groupby(data_time)]

    new_time.remove('Сегодня')
    new_time.remove('Вчера')

    return (new_time)