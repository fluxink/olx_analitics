from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
import url_dic
import PythonApplication1

#class gui(object):
    #"""в этом класе будет описан интерфейс"""

#Переменные
categories = ["Мода и стиль", "Хобби, отдых и спорт", "Недвижимость", "Детский мир", "Животные", "Электроника", "Транспорт"]
empty = ['']

def cmbbox2_values(index):

	fashion = ["Одежда/обувь", "Аксессуары", "Красота и здоровье", "Для свадьбы", "Наручные часы", "Подарки", "Мода разное"]
	hobby = ["Антиквариат/коллекции", "Книги/журналы", "Спорт/отдых", "CD/DVD/пластинки/кассеты", "Музыкальные инструменты", "Другое", "Билеты"]
	real_estate = ["Квартиры, комнаты", "Коммерческая недвижимость", "Предложения от застройщиков", "Дома", "Гаражи/парковки", "Недвижимость за рубежом", "Земля", "Посуточная аренда жилья"]
	children = ["Детская одежда", "Детские автокресла", "Детский транспорт", "Прочие детские товары", "Детская обувь", "Детская мебель", "Кормление", "Детские коляски", "Игрушки", "Товары для школьников"]
	animals = ["Собаки", "Товары для животных", "Сельхоз животные", "Кошки", "Бесплатно(животные и вязка)", "Аквариумные рыбки", "Вязка", "Птицы", "Другие животные", "Грызуны", "Рептилии"]
	electronics = ["Телефоны и аксессуары", "Компьютеры и комплектующие", "ТВ/видеотехника", "Техника для кухни", "Аудиотехника", "Техника для дома", "Фото/видео", "Ноутбуки и аксессуары", "Аксессуары и комплектующие", "Индивидуальный уход", "Прочая электроника", "Игры и игровые приставки", "Планшеты/эл. книги и аксессуары", "Климатическое оборудование"]
	transport = ["Легковые автомобили", "Грузовые автомобили", "Автобусы", "Мото", "Спецтехника", "Сельхоз техника", "Водный транспорт", "Прицепы/Дома на колёсах", "Воздушный транспорт", "Другой транспорт"]

	kategoria = [fashion, hobby, real_estate, children, animals, electronics, transport]

	return kategoria[index]

def cmbbox2_pack(event):
	cmbbox1_2['values'] = cmbbox2_values(cmbbox1_1.current())
	cmbbox1_2.current(0)

def pack_cmbbox3_lbl3(view):
	if view == True:
		cmbbox1_3.grid(column=0, row=9, sticky=W)
		lbl1_3.grid(column=0, row=8, sticky=W)
	else:
		cmbbox1_3['values'] = empty
		cmbbox1_3.current(0)
		cmbbox1_3.grid_forget()
		lbl1_3.grid_forget()

def pack_cmbbox4_lbl4(view):
	if view == True:
		cmbbox1_4.grid(column=0, row=12, sticky=W)
		lbl1_4.grid(column=0, row=11, sticky=W)
	else:
		cmbbox1_4['values'] = empty
		cmbbox1_4.current(0)
		cmbbox1_4.grid_forget()
		lbl1_4.grid_forget()

def cmbbox4_create(event):

	computer_parts = ["Прочие комплектующие", "Видеокарты", "Жесткие диски", "Процессоры", "Модули памяти", "Материнские платы", "Корпуса", "Блоки питания", "Оптические диски", "ТВ-тюнеры"]
	peripherals = ["Копиры", "Сетевое оборудование", "Прочие периферийные устройства", "Клавиатуры, мыши, манипуляторы", "Вебкамеры", "Компьтерная акустика", "Принтеры", "МФУ", "Сканеры"]

	pack_cmbbox4_lbl4(False)

	if cmbbox1_1.current() == 5:
		if cmbbox1_2.current() == 1:
			if cmbbox1_3.current() == 0:
				cmbbox1_4['values'] = computer_parts
				cmbbox1_4.current(0)
				pack_cmbbox4_lbl4(True)

			if cmbbox1_3.current() == 1:
				cmbbox1_4['values'] = peripherals
				cmbbox1_4.current(0)
				pack_cmbbox4_lbl4(True)

def cmbbox3_create(event):

	odezhda = ["Женская одежда", "Женская обувь", "Мужская одежда", "Мужская обувь", "Женское белье/купальники", "Головные уборы", "Одежда для беременных", "Мужское белье"]
	aksessuary = ["Сумки", "Другие аксессуары", "Бижутерия", "Ювелирные изделия"]
	krasota = ["Прочие товары", "Парфюмерия", "Косметика", "Средства по уходу", "Оборудование парикмахерских/салонов красоты", "Товары для инвалидов"]
	svadba = ["Свадебные платья", "Свадебные аксессуары"]

	antikvariat = ["Коллекционирование", "Поделки/рукоделие", "Живопись", "Букинистика", "Предметы искусства", "Антикварная мебель"]
	sport = ["Вело", "Атлетика/фитнес", "Охота/рыбалка", "Туризм", "Прочие виды спорта", "Футбол", "Роликовые коньки", "Настольные игры", "Единоборства/бокс", "Лыжи/сноуборды", "Водные виды спорта", "Коньки", "Игры с ракеткой", "Хоккей"]
	music_instruments = ["Студийное оборудование", "Аксессуары для музыкальных интрументов", "Прочее", "Пианино, фортепиано, рояли", "Духовые инструменты", "Акустические гитары", "Электрогитары", "Синтезаторы", "Ударные интрументы", "Комбоусилители", "Бас гитары"]

	kvartiry_komnaty = ["Продажа квартир, комнат", "Аренда квартир, комнат"]
	commercial = ["Аренда коммерческой недвижимости", "Продажа коммерческой недвижимости"]
	houses = ["Продажа домов", "Аренда домов"]
	garazhy = ["Продажа гаражей/парковок", "Аренда гаражей/парковок"]
	zemlya = ["Продажа земли", "Аренда земли"]
	posutochno = ["Квартиры", "Дома", "Хостелы", "Комнаты", "Отели"]

	detskaya_odezhda = ["Для мальчиков", "Для девочек", "Для новорожденных"]

	phones = ["Мобильные телефоны/смартфоны", "Аксессуары для телефонов", "Стационарные телефоны", "Запчасти для телефонов", "Рации и прочие телефоны", "Симкарты, тарифы, номера"]
	computers = ["Комплектующие и аксессуары", "Периферийные устройства", "Настольные компьютеры", "Мониторы", "Расходные материалы", "Внешние накопители", "Другое", "Серверы"]
	tv = ["Телевизоры", "Аксессуары для ТВ и видеотехники", "Прочая ТВ, видеотехника", "DVD плееры", "Спутниковое ТВ", "Проекторы"]
	kitchen = ["Прочая техника для кухни", "Холодильники", "Плиты/печи", "Кофеварки/кофемолки", "Кухонные комбайны и измельчители", "Пароварки", "Электрочайники", "Микроволновые печи", "Посудомоечные машины", "Хлебопечки", "Вытяжки"]
	audio = ["Наушники", "Акустические системы", "Портативная акустика", "Прочая аудиотехника", "Усилители/ресиверы", "Радиоприемники", "Магнитолы", "Музикальные центры", "CD/MD/виниловые проигрыватели", "MP3 плееры"]
	for_home = ["Стиральные машины", "Прочая техника для дома", "Швейные машины и оверлоки", "Пылесосы", "Утюги", "Фильтры для воды", "Вязальные машины"]
	foto_video = ["Цифровые фотоапарраты", "Аксессуары для фото/видеокамер", "Пленочные фотоапарраты", "Видеокамеры", "Объективы", "Экшн-камеры", "Телескопы/бинокли", "Штативы/монопады", "Фотовспышки"]
	notebooks = ["Ноутбуки", "Запчасти для ноутбуков", "Аксессуары для ноутбуков"]
	individualnyy_uhod = ["Электронные сигареты, вапорайзеры и аксессуары", "Фены, укладка волос", "Прочая техника для индивидуального ухода", "Бритвы, эпиляторы, машинки для стрижки", "Весы"]
	games = ["Игры для приставок", "Приставки", "Аксессуары", "Герои игр", "Игры для ПК"]
	tablets = ["Планшетные компьютеры", "Аксессуары для планшетов, эл. книг", "Запчасти для планшетов, эл. книг", "Электронные книги", "Графические планшеты"]

	pack_cmbbox3_lbl3(False)

	if cmbbox1_1.current() == 0:
		if cmbbox1_2.current() == 0:
			cmbbox1_3['values'] = odezhda
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 1:
			cmbbox1_3['values'] = aksessuary
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 2:
			cmbbox1_3['values'] = krasota
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)		

		if cmbbox1_2.current() == 3:
			cmbbox1_3['values'] = svadba
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

	if cmbbox1_1.current() == 1:
		if cmbbox1_2.current() == 0:
			cmbbox1_3['values'] = antikvariat
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 2:
			cmbbox1_3['values'] = sport
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 4:
			cmbbox1_3['values'] = music_instruments
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

	if cmbbox1_1.current() == 2:
		if cmbbox1_2.current() == 0:
			cmbbox1_3['values'] = kvartiry_komnaty
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 1:
			cmbbox1_3['values'] = commercial
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 3:
			cmbbox1_3['values'] = houses
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 4:
			cmbbox1_3['values'] = garazhy
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 6:
			cmbbox1_3['values'] = zemlya
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 7:
			cmbbox1_3['values'] = posutochno
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

	if cmbbox1_1.current() == 3:
		if cmbbox1_2.current() == 0:
			cmbbox1_3['values'] = detskaya_odezhda
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

	if cmbbox1_1.current() == 5:
		if cmbbox1_2.current() == 0:
			cmbbox1_3['values'] = phones
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 1:
			cmbbox1_3['values'] = computers
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 2:
			cmbbox1_3['values'] = tv
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 3:
			cmbbox1_3['values'] = kitchen
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 4:
			cmbbox1_3['values'] = audio
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 5:
			cmbbox1_3['values'] = for_home
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 6:
			cmbbox1_3['values'] = foto_video
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 7:
			cmbbox1_3['values'] = notebooks
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 9:
			cmbbox1_3['values'] = individualnyy_uhod
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 11:
			cmbbox1_3['values'] = games
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

		if cmbbox1_2.current() == 12:
			cmbbox1_3['values'] = tablets
			cmbbox1_3.current(0)
			pack_cmbbox3_lbl3(True)

def event_cmbbx1(event):
	event1 = event
	cmbbox2_pack(event1)
	cmbbox3_create(event1)
	cmbbox4_create(event1)

def event_cmbbx2(event):
	event1 = event
	cmbbox3_create(event1)
	cmbbox4_create(event1)

def start_pars():
	url = url_dic.get_way(index_category=cmbbox1_1.get(), index_subcategory=cmbbox1_2.get(), index_section=cmbbox1_3.get(), index_subsection=cmbbox1_4.get(), request=search_request.get())
	print(url)
	file_name = fd.asksaveasfilename(filetypes=(("CSV Files", "*.csv"),)) + '.csv'
	PythonApplication1.start(url, file_name)

root = Tk()
root.title('OLX Analitics')
root.geometry('400x600')

search_request = StringVar()

nb = Notebook(root)
tab1 = Frame(nb)
tab2 = Frame(nb)
nb.add(tab1, text='Первая')
nb.add(tab2, text='Вторая')

lbl1_0 = Label(tab1, text='Поисковой запрос')
lbl1_0.grid(column=0, row=0, sticky=W)

entry_search = Entry(tab1, width=30, textvariable = search_request)
entry_search.grid(column=0, row=1, sticky=W)

lbl1_1 = Label(tab1, text='Категория')
lbl1_1.grid(column=0, row=2, sticky=W)
cmbbox1_1 = Combobox(tab1, values=categories, state='readonly')
cmbbox1_1.current(0)
cmbbox1_1.grid(column=0, row=3, sticky=W)
cmbbox1_1.bind("<<ComboboxSelected>>", event_cmbbx1)

lbl1_2 = Label(tab1, text='Подкатегория')
lbl1_2.grid(column=0, row=5, sticky=W)
cmbbox1_2 = Combobox(tab1, values=cmbbox2_values(cmbbox1_1.current()), width=30, state='readonly')
cmbbox1_2.current(0)
cmbbox1_2.grid(column=0, row=6)
cmbbox1_2.bind("<<ComboboxSelected>>", event_cmbbx2)

lbl1_3 = Label(tab1, text='Раздел')
cmbbox1_3 = Combobox(tab1, width=30, state='readonly')
cmbbox1_3.bind("<<ComboboxSelected>>", cmbbox4_create)

lbl1_4 = Label(tab1, text='Подраздел')
cmbbox1_4 = Combobox(tab1, state='readonly', width=30)

start_button = Button(tab1, text='Кнопачка', command=start_pars)
start_button.grid(column=0, row=13)



nb.pack(expand=1, fill='both')

root.mainloop()