
'''Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''

from function import *

try:
    phone_book = load()
except:
    phone_book = {
        "иванов иван иванович": {"mobilephone": ["79370757270", "79370756666"], "birthday": ["13-08-1984"], "email": ["ivan_v@yandex.ru"]},
        "петров петр петрович": {"mobilephone": ["79161100000", "79161122222"], "birthday": ["01-01-1990"], "email": ["petr_p@yandex.ru"]}}
    save(phone_book)
    print("Не удалось загрузить телефонную книгу. Создана тестовая телефонная книга.\n")

choice = None
while choice != 0:
    menu()
    choice = int(input("Введите пункт меню (цифру): "))
    match choice:
        case 0: print('\nВы вышли из программы. До свидания')
        case 1: save(phone_book)
        case 2: load()
        case 3: print_all_data_contact()            
        case 4: print_phones_contact()
        case 5: print_all_fullname()
        case 6: create_new_contant()
        case 7: delete_contact()
        case 8: edit_contact()
        case 9: add_data()
        case _: print("\nВыбирете пункт меню или выйдите из программы (Цифра: 0)\n")