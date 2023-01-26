import model
def main_menu():
    menu_list = ['Показать все контакты',
        'Открыть файл',
        'Сохранить файл',
        'Создать контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Найти контакт',
        'Выход']

    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    print()
        #Сделать проверку на дурака
    user_input = int(input('Введи номер меню: '))
    print()
    return user_input

def show_all (db: list):
    if len(db) > 0:
        for i in range(len(db)):
            user_id = i + 1
            print(user_id, end='. ')
            for k in db[i].values():
                print(f'{k}', end=' ')
            print()
        print()
    else:
        print('Телефонная книга пуста, или не открыта. Сначала нужно открыть книгу')
        print()

def exit_programm():
    print('Завершение работы программы')
    exit()

def create_contact():
    print('Создание нового контакта')
    new_contact = dict()
    new_contact['surname'] = input('Введите фамилию: ')
    new_contact['name'] = input('Введите имя: ')
    new_contact['phone'] = input('Введите номер телефона: ')
    new_contact['type'] = input('Введите тип телефона: ')
    return  new_contact

def chose_num():
    number_change = input('Выберите номер: ')
    print()
    return int(number_change)
def cgange_contact(db: list):
    print('Изменение контакта')
    index_db = chose_num() - 1
    print('менять фамилию? 0 - нет, 1 - да')
    if chose_num() == 1:
        db[index_db]['surname'] = input('Введите новую фамилию')
    print('менять имя? 0 - нет, 1 - да')
    if chose_num() == 1:
        db[index_db]['name'] = input('Введите новое имя')
    print('менять телефон? 0 - нет, 1 - да')
    if chose_num() == 1:
        db[index_db]['phone'] = input('Введите новый телефон')
    print('менять тип телефона? 0 - нет, 1 - да')
    if chose_num() == 1:
        db[index_db]['type'] = input('Введите новый тип телефона')

def save_book(db: list):
    with open('data.txt', 'w') as file:
        finish = ''
        for i in range(len(db)):
            for element in db[i].values():
                finish += (element + ';')
            finish += '\n'
        file.write(finish)

def delete_contact(db: list):
    print('Удаление контакта, укажите номер удаляемого контакта')
    index_db = chose_num()-1
    db.pop(index_db)


def write_surname():
    surname = input('Укажите фамилию для поиска контакта: ')
    return surname

def search_contact(db: list, surname: str):
    for i in range(len(db)):
        for element in db[i].values():
            if surname in element:
                print(*db[i].values())
                print()
        else:
            print('Такого контакта нет')
            print()
            break


