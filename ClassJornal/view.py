import model

def input_class():
    return input('Введите номер и букву класса : ').upper()

def input_subject():
    return input('Введите название предмета : ').lower()

def who_answer():
    return input('Выберите кого проверить : ')

def what_mark():
    return input('Введите оценку за ответ : ')

def table_columns():
    print('Список учеников        Список оценок')

def wrong_subject():
    return('Такого предмета не существует, введите правильный предмет')

def wrong_student():
    return('Такого студента не существует, проверьте правильность имени')

def file_error():
    return ('Такого класса не существует, пожалуйста перезапустите программу')

def list_of_child(journal: dict):
    for i, childe in enumerate(journal, 1):
        print(f'{i}. {childe:20} {journal.get(childe)}')