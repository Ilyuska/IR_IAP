print('\n\n\n\n')
song_list = [] #Хранение всего списка 

class Song: #Класс для каждого элемента списка
    def __init__(self, artist, title, album, year, duration, listens): #Инициализация элемента
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
        self.duration = duration
        self.listens = listens


def Menu():
    print ("Выберите пункут меню: \n 1. Показать весь список \n 2. Добавить элемент \n 3. Удалить элемент \n 4. Изменить элемент \n 5. Весь отсортированный список \n 6. Отсортированный список песен одного исполнителя \n 7. Отсортированный список песен определеноого периода \n 8. Завершить программу")
    try:
        x = int(input())
    except:
        print ("Введены некорректные данные, попробуйте снова.")
        Menu()
    while x!=8:
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
            for x in song_list:
                if x.artist == singer:
                        new_list.append(x)
            PrintList(SortOneSinger(new_list))
        elif x == 7:
            years = input("Введите через пробел какие года вас интересуют:\n").strip().split()
            try:
                new_list = []
                for x in song_list:
                    if int(years[0]) <= int(x.year) <= int(years[1]):
                        new_list.append(x)
                PrintList(SortForYears(new_list))
            except:
                print("Введены некорректные данные")
        else:
            print ("Введены некорректные данные, попробуйте снова.")
        Menu()
    CloseProgram()


def CloseProgram():
    wannaSave = input("Сохранить изменения базы данных? (Y/N)")
    if wannaSave == "Y":
        with open('input.txt', 'w') as file:
            for i in song_list:
                file.write(f'{i.artist};{i.title};{i.album};{i.year};{i.duration};{i.listens}\n')
        exit("Программа завершена с сохранением")
    elif wannaSave == "N":
        exit("Программа завершена без сохранения")
    else:
        print ("Ввдены некорректные данные") 
        Menu()



def Read (): #Считываем весь файл
    with open('input.txt', 'r') as file:
        for line in file:
            artist, title, album, year, duration, listens = line.strip().split(';')
            song_list.append(Song(artist, title, album, year, duration, listens))


def PrintList (listt): #Печать переданного списка
    try:
        id = 1
        for i in listt:
            print(f'id: {id} Artist: {i.artist}, Title: {i.title}, Album: {i.album}, Year: {i.year}, Duration: {i.duration}, Listens: {i.listens}')
            id+=1
    except:
        print("Список пуст")


def AddElement (): #Добавление элемента 
    song = input("Введите новую запись в формате: Исполнитель;Название песни;Альбом;Год выпуска;Длительность;Количетсво прослушиваний\nЕсли хотите вернуться введите 0\n")
    try:
        artist, title, album, year, duration, listens = song.strip().split(';')
        song_list.append(Song(artist, title, album, int(year), duration, int(listens)))
        print ("Успешно добавленно")
    except:
        try: 
            if int(song) == 0: return 0 
        except: 
            print ("Ошибка ввода, попробуйте снова:") 


def ChooseElement(elem):
    try:
        if int(elem)-1>=len(song_list):
            print("Такого элемента нету!")
        else: 
            return int(elem)-1
    except:
        id = 1
        for i in song_list:
            if i.title.strip() == elem.strip(): #.strip убирает лишние пробелы
                return id-1
            id+=1
        print("Такого элемента нету!")


def DeleteElement (idElem):
    if idElem is None:
        idElem = input("Введите id или название песни для удаления:")
    try:
        elem = song_list[ChooseElement(idElem)]
        if ChooseElement(idElem)>=0:
            print(f'Удален элемент: \n {elem.artist};{elem.title};{elem.album};{elem.year};{elem.duration};{elem.listens}')
            song_list.pop(ChooseElement(idElem))
    except:
        print()


def СhangeElement():
    idElem = input("Введите id или название песни для изменения:")
    try:
        elem = song_list[ChooseElement(idElem)]
        print(f'Выбранный элемент: \n {elem.artist};{elem.title};{elem.album};{elem.year};{elem.duration};{elem.listens}')
        AddElement()
        song_list.pop(ChooseElement(idElem))
    except:
        print()


def SortAll(new_list):
    if len(new_list) <= 1:
        return new_list
    else:
        pivot = new_list[len(new_list) // 2]
        left, middle, right = [], [], []
        for x in new_list:
            if x.artist < pivot.artist:
                left.append(x)
            elif x.artist == pivot.artist:
                if int(x.year) > int(pivot.year):
                    left.append(x)
                elif int(x.year) == int(pivot.year):
                    if int(x.listens) > int(pivot.listens):
                        left.append(x)
                    elif int(x.listens) == int(pivot.listens):
                        middle.append(x)
                    else:
                        right.append(x)
                else:
                    right.append(x)
            else:
                right.append(x)
        return SortAll(left) + middle + SortAll(right)


def SortOneSinger(new_list):
    if len(new_list) <= 1:
        return new_list
    else:
        pivot = new_list[len(new_list) // 2]
        left, middle, right = [], [], []
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
        return SortAll(left) + middle + SortAll(right)


def SortForYears(new_list):
    if len(new_list) <= 1:
        return new_list
    else:
        pivot = new_list[len(new_list) // 2]
        left, middle, right = [], [], []
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
        return SortAll(left) + middle + SortAll(right)

Read()
Menu()