import json
import os

def menu():  # 0 - Выход из программы
    print('Меню: ',
          '0 - Выход из программы',
          '1 - Сохранить в удаленном хранилище',
          '2 - Загрузить данные из удаленного хранилища',
          '3 - Вывести по ФИО все данные контакта',
          '4 - Вывести по ФИО телефоны',
          '5 - Вывести все контакты',
          '6 - Создать новый контакт',
          '7 - Удалить контакт',
          '8 - Редактировать контакт',
          '9 - Добавить контактые данные', sep='\n')
    
def save(phone_book):  # 1 - Сохранение данных в удаленном хранилище
    os.system('cls||clear')
    with open('phone_book.json', 'w', encoding='utf-8') as pb:
        pb.write(json.dumps(phone_book, ensure_ascii=False, indent=4))
    print('\nТелефонная книга успешно сохранена в удаленное хранилище\n')


def load():  # 2 - Загрузка данных из удаленного хранилища
    os.system('cls||clear')
    with open('phone_book.json', 'r', encoding='utf-8') as pb: pb_local = json.load(pb)
    print('\nТелефонная книга из удаленного хранилища успешно загружена\n')
    return pb_local

def print_all_data_contact():  # 3 - вывести по ФИО все данные контакта
    pb_local = load()
    print_all_fullname()
    f_name = pb_local.get(input("Введите ФИО для поиска всех данных: ").lower().strip(), None)
    if f_name != None:
        for k, v in f_name.items():
            if type(v) == list:
                for i in range(len(v)):
                    print(k, v[i], sep=' ', end='\n')
            else:
                print(k, v)
    else:
        print('\nТакого контакта нет')
    print()


def print_phones_contact():  # 4 - вывести по ФИО телефоны
    pb_local = load()
    print_all_fullname()
    f_name = pb_local.get(input("Введите ФИО для поиска всех телефонов: ").lower().strip(), None)
    if f_name != None:
        for k, v in f_name.items():
            if (k == 'mobilephone' or k == 'workphone'):
                for i in range(len(v)):
                    print(k, v[i], sep=' ', end='\n')
    else: print('\nТакого контакта нет')
    print()


def print_all_fullname():  # 5 - вывести все контакты
    os.system('cls||clear')
    pb_local = load()
    print("Список контактов в телефонной книге:")
    [print(' ', k) for k in pb_local.keys()]
    print()

def choose_data_type():
    type_data = None
    flag = True
    while flag:
        print('Выбирете какие данные добавить: ', '1 - mobilephone', '2 - workphone', '3 - email', '4 - birthday', sep='\n')
        type_data = input('Выбирете цифру (тип телефона): ')
        match type_data:
            case '1':
                type_data = 'mobilephone'
                flag = False
            case '2':
                type_data = 'workphone'
                flag = False
            case '3':
                type_data = 'email'
                flag = False
            case '4':
                type_data = 'birthday'
                flag = False
            case _: flag = True
    return type_data

def create_new_contant():  # 6 - создать новый контакт
    pb_local = load()
    print_all_fullname()
    print('Введите ФИО нового контакта по образцу: Иванов Иван Иванович')
    f_name = input("Введите ФИО: ").lower().strip()
    if f_name in pb_local:
        return print("\033[31m {} \033[0m" .format('\nТакой контакт существует. Выбирете пункт 9 в меню - добавить контактые данные\n'))

    type_data = choose_data_type()

    inp_data = input("Введите данные: ")
    pb_local.update({f_name: {'mobilephone': [], 'workphone': [], 'email': [], 'birthday': []}})
    pb_local[f_name][type_data].append(inp_data)
        
    save(pb_local)
    print('Создан контакт и добавлены данные\n')


def delete_contact():  # 7 - удалить контакт
    pb_local = load()
    print_all_fullname()

    print('\nОбразец для ввода ФИО: Иванов Иван Иванович')
    f_name = input("Введите ФИО, контака который вы хотите удалить: ").lower().strip()
    answer = pb_local.get(f_name, None)
    if answer != None:
        pb_local.pop(f_name)
        save(pb_local)
        print('Контакт удалён.\n')
    else: print('\nТакого контакта нет\n')

def edit_contact():  # 8 - редактировать телефонную книгу
    pb_local = load()
    print_all_fullname()

    f_name = input("Введите ФИО контакта который вы хотите редактировать: ").lower().strip()
    answer = pb_local.get(f_name, None)
    if answer != None:
        count = 0
        dict_res = {}
        print('\nСписок данных доступных для изменения: ')
        for k, v in pb_local[f_name].items():
            if len(v) > 0:
                for i in v:
                    dict_res[count] = [k, i]
                    print(count, k, i)
                    count += 1         
            else:
                dict_res[count] = [k, v]
                print(count, k, v)
                count += 1

        type_data = None
        flag = True
        while flag:
            type_data = int(input('Выбирете цифру (0, 1, 2 ...). Данные, которые хотите изменить: '))
            if dict_res.get(type_data, 0) != 0:
                try: position = pb_local[f_name][dict_res[type_data][0]].index(dict_res[type_data][1])
                except: position = -1

                if position >= 0: pb_local[f_name][dict_res[type_data][0]][position] = input('Введите новые данные: ')
                else: pb_local[f_name][dict_res[type_data][0]] = [(input('Введите новые данные: '))]

                flag = False
            
        save(pb_local)
        print('Контакт отредактирован\n')
    else: print('\nТакого контакта нет\n')


def add_data():  # 9 - добавить контактые данные
    pb_local = load()
    print_all_fullname()

    f_name = input("В какой контакт вы хотите добавить данные: ").lower().strip()   
    type_data = choose_data_type()
    inp_data = input("Введите данные для добавления: ")
    if type(pb_local[f_name][type_data]) == list: pb_local[f_name][type_data].append(inp_data)
    else: pb_local[f_name][type_data] = inp_data
        
    save(pb_local)
    print('\nНовые данные добавлены\nТелефонная книга успешно сохранена в удаленное хранилище\n')