song_list = [] #Хранение всего списка 

class Song: #Класс для каждого элемента списка
    def __init__(self, artist, title, album, year, duration, listens): #Инициализация элемента
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
        self.duration = duration
        self.listens = listens


def Menu(): #Рекурсивная функция меню
    print ("""
    Выберите пункут меню: 
      1. Показать весь список 
      2. Добавить элемент 
      3. Удалить элемент 
      4. Изменить элемент 
      5. Отсортировать весь список 
      6. Отсортировать список песен одного исполнителя 
      7. Отсортировать список песен определенного периода 
      8. Завершить программу
    """)
    try: #Обработка ошибки ввода
        x = int(input()) #Считывание выбранного пункта
    except:
        print ("Введены некорректные данные, попробуйте снова.")
        Menu()
    while x!=8: #Переключатель пунктов
        if x == 1:
            PrintList(song_list)
        elif x == 2:
            AddElement()
        elif x == 3:
            DeleteElement(None)
        elif x == 4:
            СhangeElement()
        elif x == 5:
            PrintList(SortAll(song_list))
        elif x == 6:
            singer = input("Введите исполнителя:\n")
            new_list = []
            for x in song_list: #Создание подсписка нужный исполнителей
                if x.artist == singer:
                        new_list.append(x)
            if len(new_list)==0:
                print("Ничего не найдено")
            else:
                PrintList(SortOneSinger(new_list))
        elif x == 7:
            years = input("Введите через пробел какие года вас интересуют:\n").strip().split()
            try:
                new_list = []
                for x in song_list: #Создание подсписка нужного периода времени
                    if int(years[0]) <= int(x.year) <= int(years[1]):
                        new_list.append(x)
                if len(new_list)==0:
                    print("Введены некорректные данные")
                else:
                    PrintList(SortForYears(new_list))
                
            except:
                print("Введены некорректные данные")
        else:
            print ("Введены некорректные данные, попробуйте снова.")
        Menu() #Рекурсивный вызов меню
    CloseProgram() #Если ввели 8 (захотели выйти), то вызов этой функции


def CloseProgram(): #Функция закрывающая программу
    wannaSave = input("Сохранить изменения базы данных? (Y/N)") 
    if wannaSave == "Y": #Обработка сохранения (нужно или нет)
        with open('input.txt', 'w') as file:
            for i in song_list:
                file.write(f'{i.artist};{i.title};{i.album};{i.year};{i.duration};{i.listens}\n')
        exit("Программа завершена с сохранением") #Выход из программы
    elif wannaSave == "N":
        exit("Программа завершена без сохранения") #Выход из программы
    else:
        print ("Ввдены некорректные данные") #Если пользователь ввел чтото другое то заново в меню идем
        Menu()



def Read (): #Считываем весь файл
    with open('input.txt', 'r') as file:
        for line in file:
            artist, title, album, year, duration, listens = line.strip().split(';')
            song_list.append(Song(artist, title, album, year, duration, listens))


def PrintList (listt): #Печать переданного списка
    try:
        for index, item in enumerate(listt, start=1): #Используем enumerate для индексирования элементов для удобного вывода
            print(f'id: {index} Artist: {item.artist}, Title: {item.title}, Album: {item.album}, Year: {item.year}, Duration: {item.duration}, Listens: {item.listens}')
    except:
        print("Список пуст")


def AddElement (): #Добавление элемента 
    song = input("""Введите новую запись в формате: Исполнитель;Название песни;Альбом;Год выпуска;Длительность;Количетсво прослушиваний
Если хотите вернуться введите 0
""")
    try: #Если введены корретные данный и можно их засплитить и пихнуть то делаем это 
        artist, title, album, year, duration, listens = song.strip().split(';')
        song_list.append(Song(artist, title, album, int(year), duration, int(listens)))
        print ("Успешно добавленно")
    except: #Если не получается 
        try: #Попытаться понять не хочет ли пользователь просто не добавлять ничего
            if int(song) == 0: return 0 #Если не хочет то просто выходим из функции
            else:
                print ("Ошибка ввода")
                return 0 
        except: 
            print ("Ошибка ввода") 
            return 0


def ChooseElement(elem):#Ищет id элемента в списке
    try:
        if int(elem)-1>=len(song_list): #Если не влезает в границы списка то выходим
            print("Такого элемента нету!")
        else: #Если влезает в границы списка то возвращаем индекс
            return int(elem)-1
    except:
        for id, song in enumerate(song_list, start=1):
            if song.title.strip() == elem.strip(): #Если название соответсвует какомуто из списка то возвращаме его id
                return id - 1
        print("Такого элемента нету!")


def DeleteElement (idElem):#Удаление элемента
    if idElem is None: #Проверка на пустоту id и заполнение
        idElem = input("Введите id или название песни для удаления:")
    try: 
        elem = song_list[ChooseElement(idElem)] #Поиск элемента
        if ChooseElement(idElem)>=0: #Проверка что вернули не 0
            print(f'Удален элемент: \n {elem.artist};{elem.title};{elem.album};{elem.year};{elem.duration};{elem.listens}')
            song_list.pop(ChooseElement(idElem)) #Удаляем элемент
    except:
        print()


def СhangeElement():#Изменение элемента
    idElem = input("Введите id или название песни для изменения:")
    try:
        elem = song_list[ChooseElement(idElem)]
        print(f'Выбранный элемент: \n {elem.artist};{elem.title};{elem.album};{elem.year};{elem.duration};{elem.listens}')
        if AddElement()!=0:
            song_list.pop(ChooseElement(idElem))
    except:
        print()


def SortAll(new_list):
    # Если список пуст или содержит только один элемент, то он уже отсортирован
    if len(new_list) <= 1:
        return new_list
    else:
        # Выбираем опорный элемент из середины списка
        pivot = new_list[len(new_list) // 2]
        left, middle, right = [], [], []

        # Разделяем список на три части: меньше, равные и больше опорного элемента по имени
        for x in new_list:
            if x.artist < pivot.artist:
                left.append(x) #Если текущий меньше опорного то добавляем его в левую часть (по возрастанию)
            elif x.artist == pivot.artist: #Если имена артистов одинаковые то сравниваем по годам песни
                if int(x.year) > int(pivot.year):
                    left.append(x) #Если текущий больше опорного то добавляем его в левую часть (по убыванию)
                elif int(x.year) == int(pivot.year): #Если года песен одинаковые то сравниваем по кол прослушиваний
                    if int(x.listens) > int(pivot.listens): 
                        left.append(x) #Если текущий больше опорного то добавляем его в левую часть (по убыванию)
                    elif int(x.listens) == int(pivot.listens):
                        middle.append(x) #Если текущий равен опорному то добавляем его в равную часть
                    else:
                        right.append(x) #Иначе добавляем в правую
                else:
                    right.append(x)
            else: #Если текущий больше опорного то добавляем его в правую часть
                right.append(x)

        # Рекурсивно сортируем подсписки и объединяем их в один отсортированный список
        return SortAll(left) + middle + SortAll(right)



def SortOneSinger(new_list):
    # Если список пуст или содержит только один элемент, то он уже отсортирован
    if len(new_list) <= 1:
        return new_list
    else:
        # Выбираем опорный элемент из середины списка
        pivot = new_list[len(new_list) // 2]
        left, middle, right = [], [], []

        # Разделяем список на три части: меньше, равные и больше опорного элемента
        for x in new_list:
            if x.album > pivot.album:
                left.append(x)
            elif x.album == pivot.album:
                if x.title < pivot.title:
                    left.append(x)
                elif x.title == pivot.title:
                    middle.append(x)
                else:
                    right.append(x)
            else:
                right.append(x)

        # Рекурсивно сортируем подсписки и объединяем их в один отсортированный список
        return SortOneSinger(left) + middle + SortOneSinger(right)



def SortForYears(new_list):
    # Если список пуст или содержит только один элемент, то он уже отсортирован
    if len(new_list) <= 1:
        return new_list
    else:
        # Выбираем опорный элемент из середины списка
        pivot = new_list[len(new_list) // 2]
        left, middle, right = [], [], []

        # Разделяем список на три части: больше, равные и меньше опорного элемента
        for x in new_list:
            if int(x.year) > int(pivot.year):
                left.append(x)
            elif int(x.year) == int(pivot.year):
                if x.artist < pivot.artist:
                    left.append(x)
                elif x.artist == pivot.artist:
                    middle.append(x)
                else:
                    right.append(x)
            else:
                right.append(x)

        # Рекурсивно сортируем подсписки и объединяем их в один отсортированный список
        return SortForYears(left) + middle + SortForYears(right)


Read()
Menu()