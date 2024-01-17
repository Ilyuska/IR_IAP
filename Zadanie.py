print('\n\n\n\n')
song_list = [] #Хранение всего списка 

class Song: #Класс для каждого элемента списка
    def __init__(self, id, artist, title, album, year, duration, listens): #Инициализация элемента
        self.id = id
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
        self.duration = duration
        self.listens = listens


def Menu():
    print ("Выберите пункут меню: \n 1. Показать весь список \n 2. Добавить элемент \n 3. Удалить элемент \n 4. Изменить элемент \n 5. Весь отсортированный список \n 6. Список песен одного исполнителя \n 7. Список песен определеноого периода \n 8. Завершить программу")
    x = int(input())
    while x!=8:
        if x == 1:
            PrintList(song_list)
        elif x == 2:
            AddElement()
        elif x == 3:
            DeleteElement(None)
        elif x == 4:
            СhangeElement()
        # elif x == 5:
        #     SortAll()
        # elif x == 6:
        #     SortOneSinger()
        # elif x == 7:
        #     SortForYears()
        else:
            print ("Введены некорректные данные, попробуйте снова.")
        Menu()
    exit()   


def Read (): #Считываем весь файл
    with open('input.txt', 'r') as file:
        id = 1
        for line in file:
            artist, title, album, year, duration, listens = line.strip().split(';')
            song_list.append(Song(id,artist, title, album, year, duration, listens))
            id+=1


def PrintList (listt): #Печать переданного списка
    for i in listt:
        print(f'id: {i.id} Artist: {i.artist}, Title: {i.title}, Album: {i.album}, Year: {i.year}, Duration: {i.duration}, Listens: {i.listens}')


def AddElement (): #Добавление элемента 
    song = input("Введите новую запись в формате: Исполнитель;Название песни;Альбом;Год выпуска;Длительность;Количетсво прослушиваний\nЕсли хотите вернуться введите 0\n")
    try:
        artist, title, album, year, duration, listens = song.strip().split(';')
        song_list.append(Song(len(song_list)+1,artist, title, album, year, duration, listens))
    except:
        return 0 if song == 0 else print ("Ошибка ввода, попробуйте снова:") 


def ChooseElement(elem):
    try:
        if int(elem)-1>=len(song_list):
            print("Такого элемента нету!")
        else: 
            return int(elem)-1
    except:
        for i in song_list:
            if i.title.strip() == elem.strip(): #.strip убирает лишние пробелы
                return i.id-1
        print("Такого элемента нету!")


def DeleteElement (idElem):
    if idElem is None:
        idElem = input("Введите id или название песни для удаления:")
    try:
        elem = song_list[ChooseElement(idElem)]
        if ChooseElement(idElem)>0:
            print(f'Удален элемент: \n {elem.id};{elem.artist};{elem.title};{elem.album};{elem.year};{elem.duration};{elem.listens}')
            song_list.pop(ChooseElement(idElem))
    except:
        print()


def СhangeElement():
    idElem = input("Введите id или название песни для изменения:")
    try:
        elem = song_list[ChooseElement(idElem)]
        print(f'Выбранный элемент: \n {elem.id};{elem.artist};{elem.title};{elem.album};{elem.year};{elem.duration};{elem.listens}')
        AddElement()
    except:
        print()
    

Read()
Menu()