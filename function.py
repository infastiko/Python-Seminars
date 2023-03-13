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