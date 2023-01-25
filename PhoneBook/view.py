def main_menu():
    menu_list = ['Показать все контакты',
        'Открыть файл',
        'Сохранить файл',
        'Создать контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Выход']
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
        #Сделать проверку на дурака
    user_input = int(input('Введи номер меню: '))
    return  user_input

def show_all (db: list):
    for i in range(len(db)):
        user_id = i + 1
        print(user_id, end='. ')
        for k in db[i].values():
            print(f'{k}', end=' ')
        print()


