from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import tix
import webbrowser
import url_dic
import PythonApplication1
import Post
import csv_failik
import process
from shutil import copyfile

#class gui(object):
    #"""в этом класе будет описан интерфейс"""

#Переменные
categories = ["Мода и стиль", "Хобби, отдых и спорт", "Недвижимость", "Детский мир", "Животные", "Электроника", "Транспорт"]
empty = ['']

def open_file():
    global file_name
    file_name = fd.askopenfilename(filetypes=(("CSV Files", "*.csv"),))

    process_file(file_name)

def save_file():
    global file_name
    file_path = fd.asksaveasfilename(filetypes=(('CSV Files', '*.csv'),)) + '.csv'
    copyfile(file_name, file_path)

class Datawindow():

    def main(self):
        self.search_request = StringVar()

        self.data_window = Toplevel(root)
        self.data_window.title('Сбор данных')
        self.data_window.geometry('290x250')
        self.data_window.grab_set()
        self.data_window.focus()

        self.lbl1_0 = Label(self.data_window, text='Поисковой запрос')
        self.lbl1_0.grid(column=0, row=0, sticky=W)

        self.entry_search = Entry(self.data_window, width=30, textvariable = self.search_request)
        self.entry_search.grid(column=0, row=1, sticky=W)

        self.lbl_page = Label(self.data_window, text='Число страниц')
        self.lbl_page.grid(column=1, row=0, sticky=W)
        
        vcmd = (self.data_window.register(self.callback))

        self.number_pages = Spinbox(self.data_window, from_=1, to=1000, textvariable=number_of_pages, width=5, validate='all', validatecommand=(vcmd, '%P'))
        self.number_pages.grid(column=1, row=1)

        self.lbl1_1 = Label(self.data_window, text='Категория')
        self.lbl1_1.grid(column=0, row=2, sticky=W)
        self.cmbbox1_1 = Combobox(self.data_window, values=categories, state='readonly')
        self.cmbbox1_1.current(0)
        self.cmbbox1_1.grid(column=0, row=3, sticky=W)
        self.cmbbox1_1.bind("<<ComboboxSelected>>", self.event_cmbbx1)

        self.lbl1_2 = Label(self.data_window, text='Подкатегория')
        self.lbl1_2.grid(column=0, row=5, sticky=W)
        self.cmbbox1_2 = Combobox(self.data_window, values=self.cmbbox2_values(self.cmbbox1_1.current()), width=30, state='readonly')
        self.cmbbox1_2.current(0)
        self.cmbbox1_2.grid(column=0, row=6)
        self.cmbbox1_2.bind("<<ComboboxSelected>>", self.event_cmbbx2)

        self.lbl1_3 = Label(self.data_window, text='Раздел')
        self.cmbbox1_3 = Combobox(self.data_window, width=30, state='readonly')
        self.cmbbox1_3.bind("<<ComboboxSelected>>", self.cmbbox4_create)

        self.lbl1_4 = Label(self.data_window, text='Подраздел')
        self.cmbbox1_4 = Combobox(self.data_window, state='readonly', width=30)

        self.start_button = Button(self.data_window, text='Кнопачка', command=self.start_pars)
        self.start_button.grid(column=0, row=13)

        #self.data_window.mainloop()

    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def event_cmbbx1(self, event):
        event1 = event
        self.cmbbox2_pack(event1)
        self.cmbbox3_create(event1)
        self.cmbbox4_create(event1)

    def event_cmbbx2(self, event):
        event1 = event
        self.cmbbox3_create(event1)
        self.cmbbox4_create(event1)

    def cmbbox2_values(self, index):

        fashion = ["Одежда/обувь", "Аксессуары", "Красота и здоровье", "Для свадьбы", "Наручные часы", "Подарки", "Мода разное"]
        hobby = ["Антиквариат/коллекции", "Книги/журналы", "Спорт/отдых", "CD/DVD/пластинки/кассеты", "Музыкальные инструменты", "Другое", "Билеты"]
        real_estate = ["Квартиры, комнаты", "Коммерческая недвижимость", "Предложения от застройщиков", "Дома", "Гаражи/парковки", "Недвижимость за рубежом", "Земля", "Посуточная аренда жилья"]
        children = ["Детская одежда", "Детские автокресла", "Детский транспорт", "Прочие детские товары", "Детская обувь", "Детская мебель", "Кормление", "Детские коляски", "Игрушки", "Товары для школьников"]
        animals = ["Собаки", "Товары для животных", "Сельхоз животные", "Кошки", "Бесплатно(животные и вязка)", "Аквариумные рыбки", "Вязка", "Птицы", "Другие животные", "Грызуны", "Рептилии"]
        electronics = ["Телефоны и аксессуары", "Компьютеры и комплектующие", "ТВ/видеотехника", "Техника для кухни", "Аудиотехника", "Техника для дома", "Фото/видео", "Ноутбуки и аксессуары", "Аксессуары и комплектующие", "Индивидуальный уход", "Прочая электроника", "Игры и игровые приставки", "Планшеты/эл. книги и аксессуары", "Климатическое оборудование"]
        transport = ["Легковые автомобили", "Грузовые автомобили", "Автобусы", "Мото", "Спецтехника", "Сельхоз техника", "Водный транспорт", "Прицепы/Дома на колёсах", "Воздушный транспорт", "Другой транспорт"]

        kategoria = [fashion, hobby, real_estate, children, animals, electronics, transport]

        return kategoria[index]

    def cmbbox2_pack(self, event):
        self.cmbbox1_2['values'] = self.cmbbox2_values(self.cmbbox1_1.current())
        self.cmbbox1_2.current(0)

    def pack_cmbbox3_lbl3(self, view):
        if view == True:
            self.cmbbox1_3.grid(column=0, row=9, sticky=W)
            self.lbl1_3.grid(column=0, row=8, sticky=W)
        else:
            self.cmbbox1_3['values'] = empty
            self.cmbbox1_3.current(0)
            self.cmbbox1_3.grid_forget()
            self.lbl1_3.grid_forget()

    def pack_cmbbox4_lbl4(self, view):
        if view == True:
            self.cmbbox1_4.grid(column=0, row=12, sticky=W)
            self.lbl1_4.grid(column=0, row=11, sticky=W)
        else:
            self.cmbbox1_4['values'] = empty
            self.cmbbox1_4.current(0)
            self.cmbbox1_4.grid_forget()
            self.lbl1_4.grid_forget()

    def cmbbox4_create(self, event):

        computer_parts = ["Прочие комплектующие", "Видеокарты", "Жесткие диски", "Процессоры", "Модули памяти", "Материнские платы", "Корпуса", "Блоки питания", "Оптические диски", "ТВ-тюнеры"]
        peripherals = ["Копиры", "Сетевое оборудование", "Прочие периферийные устройства", "Клавиатуры, мыши, манипуляторы", "Вебкамеры", "Компьтерная акустика", "Принтеры", "МФУ", "Сканеры"]

        self.pack_cmbbox4_lbl4(False)

        if self.cmbbox1_1.current() == 5:
            if self.cmbbox1_2.current() == 1:
                if self.cmbbox1_3.current() == 0:
                    self.cmbbox1_4['values'] = computer_parts
                    self.cmbbox1_4.current(0)
                    self.pack_cmbbox4_lbl4(True)

                if self.cmbbox1_3.current() == 1:
                    self.cmbbox1_4['values'] = peripherals
                    self.cmbbox1_4.current(0)
                    self.pack_cmbbox4_lbl4(True)

    def cmbbox3_create(self, event):

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

        self.pack_cmbbox3_lbl3(False)

        if self.cmbbox1_1.current() == 0:
            if self.cmbbox1_2.current() == 0:
                self.cmbbox1_3['values'] = odezhda
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 1:
                self.cmbbox1_3['values'] = aksessuary
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 2:
                self.cmbbox1_3['values'] = krasota
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)		

            if self.cmbbox1_2.current() == 3:
                self.cmbbox1_3['values'] = svadba
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

        if self.cmbbox1_1.current() == 1:
            if self.cmbbox1_2.current() == 0:
                self.cmbbox1_3['values'] = antikvariat
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 2:
                self.cmbbox1_3['values'] = sport
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 4:
                self.cmbbox1_3['values'] = music_instruments
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

        if self.cmbbox1_1.current() == 2:
            if self.cmbbox1_2.current() == 0:
                self.cmbbox1_3['values'] = kvartiry_komnaty
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 1:
                self.cmbbox1_3['values'] = commercial
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 3:
                self.cmbbox1_3['values'] = houses
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 4:
                self.cmbbox1_3['values'] = garazhy
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 6:
                self.cmbbox1_3['values'] = zemlya
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 7:
                self.cmbbox1_3['values'] = posutochno
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

        if self.cmbbox1_1.current() == 3:
            if self.cmbbox1_2.current() == 0:
                self.cmbbox1_3['values'] = detskaya_odezhda
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

        if self.cmbbox1_1.current() == 5:
            if self.cmbbox1_2.current() == 0:
                self.cmbbox1_3['values'] = phones
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 1:
                self.cmbbox1_3['values'] = computers
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 2:
                self.cmbbox1_3['values'] = tv
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 3:
                self.cmbbox1_3['values'] = kitchen
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 4:
                self.cmbbox1_3['values'] = audio
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 5:
                self.cmbbox1_3['values'] = for_home
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 6:
                self.cmbbox1_3['values'] = foto_video
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 7:
                self.cmbbox1_3['values'] = notebooks
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 9:
                self.cmbbox1_3['values'] = individualnyy_uhod
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 11:
                self.cmbbox1_3['values'] = games
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

            if self.cmbbox1_2.current() == 12:
                self.cmbbox1_3['values'] = tablets
                self.cmbbox1_3.current(0)
                self.pack_cmbbox3_lbl3(True)

    def start_pars(self):
        url = url_dic.get_way(index_category=self.cmbbox1_1.get(), index_subcategory=self.cmbbox1_2.get(), index_section=self.cmbbox1_3.get(), index_subsection=self.cmbbox1_4.get(), request=self.search_request.get())
        print(url)
        global file_name
        file_name = 'olx.csv'
        PythonApplication1.start(url, file_name, number_of_pages.get())
        process_file(file_name)

def process_file(file_name):
    csv_process = csv_failik.Csv_failik()

    data = csv_process.read_csv(file_name)
    cities_list = process.cities(data)
    times = process.time_of_offers(data)

    cntof.set(str(len(data)))
    general_prices = process.avg_price_total(data)
    avgp.set(str(general_prices[0]))
    minp.set(str(general_prices[1]))
    maxp.set(str(general_prices[2]))
    ctcount.set(str(len(cities_list)))

    lbl_today_value['text'] = times['Сегодня']
    lbl_yesterday_value['text'] = times['Вчера']

    cmbbox_time['values'] = process.time_list(data)
    cmbbox_time.current(0)

    cmbbox2_1['values'] = cities_list

def time_select(event):
    csv_process = csv_failik.Csv_failik()
    data = csv_process.read_csv(file_name)
    times = process.time_of_offers(data)

    lbl_time_value['text'] = times[cmbbox_time.get()]

def select_sort(up):
    
    #list = canv_frame.grid_slaves()
    #for l in list:
        #l.grid_forget()

    csv_process = csv_failik.Csv_failik()
    data_p = csv_process.fill_posts(file_name)

    data_p.sort(key=lambda post: post.price, reverse=up)
    city_name = cmbbox2_1.get()
    table = Table_frame(data_p, city_name)

def city_select(event):
    csv_process = csv_failik.Csv_failik()
    data = csv_process.read_csv(file_name)
    data_p = csv_process.fill_posts(file_name)
    posts = Post.Post_process(data_p)

    city_name = cmbbox2_1.get()
    city_dic = process.numder_of_offers_by_cities(data)
    prices_in_city = posts.avg_price_in_city(city_name=city_name, city_count=city_dic[city_name])

    lblvalue_numder_of_offers_in_city['text'] = city_dic[city_name]
    lblvalue_avg_price_in_city['text'] = prices_in_city[0]
    lblvalue_min_price_in_city['text'] = prices_in_city[1]
    lblvalue_max_price_in_city['text'] = prices_in_city[2]
    
    frame_sort.grid(column=1, row=4, sticky=NW)
    sort_button1.grid(column=0, row=0)
    sort_button2.grid(column=1, row=0)

    table = Table_frame(data_p, city_name)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=420,height=200)

class Table_frame(LabelFrame):

    def __init__(self, data_p, city_name):
        self.frame_table = LabelFrame(canvas, text='Таблица')
        self.frame_table.grid(column=0, row=0, sticky=EW, columnspan=2)
        self.clear_table()

        myscrollbar.grid(column=2, row=0, sticky=NS)
        canv_frame.columnconfigure(2, weight=1)
        canvas.grid(column=0, row=0)
        canvas.create_window((0, 0), window=self.frame_table, anchor='nw')
        self.frame_table.bind("<Configure>", myfunction)

        titlen = Post.EditLbl(root=self.frame_table, text='Название', row=0, column=0, width=45)
        titlep = Post.EditLbl(root=self.frame_table, text='Цена', row=0, column=1, width=7)
        titled = Post.EditLbl(root=self.frame_table, text='Дата', row=0, column=2, width=15)
        row = 1
        for post in data_p:
            if post.city == city_name:
            
                name = Post.EditLbl(root=self.frame_table, text=post.name, row=row, column=0, width=45)
                price = Post.EditLbl(root=self.frame_table, text=post.price, row=row, column=1, width=7)
                date = Post.EditLbl(root=self.frame_table, text=post.date, row=row, column=2, width=15)
                name.bind(post.url)
                row=row+1

    def clear_table(self):
        list = self.frame_table.grid_slaves()
        for l in list:
            l.destroy()

root = tix.Tk()
root.title('OLX Analitics')
root.geometry('445x480')

file_name = 'olx.csv'

second_window = Datawindow()

number_of_pages = StringVar()
avgp = StringVar()
minp = StringVar()
maxp = StringVar()
cntof = StringVar()
file_path = StringVar()
ctcount = StringVar()

mainmenu = Menu(root)
root.config(menu = mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Сбор данных', command=second_window.main)
filemenu.add_command(label='Импорт данных...', command=open_file)
filemenu.add_command(label='Экспорт данных...', command=save_file)
filemenu.add_separator()
filemenu.add_command(label='Выход', command=root.destroy)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label='О программе')

mainmenu.add_cascade(label='Файл', menu=filemenu)
mainmenu.add_cascade(label='Справка', menu=helpmenu)

tab2_frame2 = LabelFrame(root ,text='Основные значения')

lbl_numder_of_offers = Label(tab2_frame2, text='Общее количество объявлений:').grid(column=0, row=2, sticky=W)
lbl_general_avg_price = Label(tab2_frame2, text='Средняя цена:').grid(column=0, row=3, sticky=W)
lbl_general_min_price = Label(tab2_frame2, text='Минимальная цена:').grid(column=0, row=4, sticky=W)
lbl_general_max_price = Label(tab2_frame2, text='Максимальная цена:').grid(column=0, row=5, sticky=W)
lbl_general_count_of_cities = Label(tab2_frame2, text='Количество городов:').grid(column=0, row=6, sticky=W)
lblvalue_number_of_offers = Label(tab2_frame2, textvariable=cntof).grid(column=1, row=2, sticky=W)
lblvalue_general_avg_price = Label(tab2_frame2, textvariable=avgp).grid(column=1, row=3, sticky=W)
lblvalue_general_min_price = Label(tab2_frame2, textvariable=minp).grid(column=1, row=4, sticky=W)
lblvalue_general_max_price = Label(tab2_frame2, textvariable=maxp).grid(column=1, row=5, sticky=W)
lblvalue_general_count_of_cities = Label(tab2_frame2, textvariable=ctcount).grid(column=1, row=6, sticky=W)

tab2_frame2.grid(column=0, row=1, sticky=EW)

lbl2_1 = Label(root, text='Город').grid(column=0, row=2, sticky=W)
cmbbox2_1 = Combobox(root, state='readonly', width=30)
cmbbox2_1.grid(column=0, row=3, sticky=W)
cmbbox2_1.bind("<<ComboboxSelected>>", city_select)

tab2_frame3 = LabelFrame(root, text='Значения по городу')

lbl_number_of_offers_in_city = Label(tab2_frame3, text='Количество объявлений:').grid(column=0, row=0, sticky=W)
lbl_avg_price_in_city = Label(tab2_frame3, text='Средняя цена по городу:').grid(column=0, row=1, sticky=W)
lbl_min_price_in_city = Label(tab2_frame3, text='Минимальная цена в городе:').grid(column=0, row=2, sticky=W)
lbl_max_price_in_city = Label(tab2_frame3, text='Максимальная цена в городе:').grid(column=0, row=3, sticky=W)

lblvalue_numder_of_offers_in_city = Label(tab2_frame3, text='-')
lblvalue_numder_of_offers_in_city.grid(column=1, row=0, sticky=W)
lblvalue_avg_price_in_city = Label(tab2_frame3, text='-')
lblvalue_avg_price_in_city.grid(column=1, row=1, sticky=W)
lblvalue_min_price_in_city = Label(tab2_frame3, text='-')
lblvalue_min_price_in_city.grid(column=1, row=2, sticky=W)
lblvalue_max_price_in_city = Label(tab2_frame3, text='-')
lblvalue_max_price_in_city.grid(column=1, row=3, sticky=W)

tab2_frame3.grid(column=0, row=4, sticky=EW)

frame1 = LabelFrame(root, text='Количество объявлений по дате')

lbl_today = Label(frame1, text='Сегодня:').grid(column=0, row=0, sticky=W)
lbl_yesterday = Label(frame1, text='Вчера:').grid(column=0, row=1, sticky=W)
lbl_today_value = Label(frame1, text='-')
lbl_yesterday_value = Label(frame1, text='-')
lbl_today_value.grid(column=1, row=0, sticky=W)
lbl_yesterday_value.grid(column=1, row=1, sticky=W)

cmbbox_time = Combobox(frame1, state='readonly', width=10)
cmbbox_time.grid(column=0, row=2, sticky=W)
cmbbox_time.bind("<<ComboboxSelected>>", time_select)

lbl_time_value = Label(frame1, text='-')
lbl_time_value.grid(column=1, row=2, sticky=W)

frame1.grid(column=1, row=1, sticky=NW)

canv_frame = Frame(root)
canv_frame.grid(column=0, row=5, sticky=EW, columnspan=2)

canvas = Canvas(canv_frame)
myscrollbar=Scrollbar(canv_frame,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

frame_sort = LabelFrame(root, text='Сортировка по цене')
sort_button1 = Button(frame_sort, text='Дорогие', command= lambda: select_sort(True))
sort_button2 = Button(frame_sort, text='Дешевые', command= lambda: select_sort(False))

#nb.pack(expand=1, fill='both')

root.mainloop()