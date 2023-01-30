journal = {}
subject = ''
path = ''
data_classes = ['7Б.txt', '7А.txt']
def set_class(class_path: str):
    global path
    path = class_path + '.txt'


#C:\Users\Саша\PycharmProjects\pythonProject\ClassJorn
#'ClassJornal/' + class_path + '.txt'
def set_subject(our_subject: str):
    global subject
    subject = our_subject

def chekc_subject():
    subject_list = []
    with open(path, 'r', encoding='UTF -8') as data:
        file = data.readlines()
        for sub in file:
            subject_list.append(sub.split(';')[0])
    if subject in subject_list:
        return False
    else:
        return True


def chekc_student(student_name: str):
    student_list = []
    with open(path, 'r', encoding='UTF -8') as data:
        file = data.readlines()
    for sub in file:
        sub = sub.split(';')
        for study in sub[1].split(', '):
            student_list.append(study.split(':')[0])
    if student_name in student_list:
        return False
    else:
        return True


def open_file():

        with open(path, 'r', encoding='UTF -8') as data:
            file = data.readlines()

        for sub in file:
            if sub.split(';')[0] == subject:
                for study in sub.split(';')[1].strip().split(', '):
                    journal[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))

def save_file():
    new_file = []
    print(journal)
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF -8') as data:
        data.write('\n'.join(new_file))

def student_mark(student: str, mark: int):
    marks = list(journal.get(student))
    marks.append(mark)
    journal[student] = marks

def get_journal():
    return journal