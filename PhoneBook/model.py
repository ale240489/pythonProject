db_list = []


def read_file(path: str):
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        db_dict = dict()
        for line in my_list:
            line = line.strip().split(';')
            db_dict['surname'] = line[0]
            db_dict['name'] = line[1]
            db_dict['phone'] = line[2]
            db_dict['type'] = line[3]
            db_list.append(db_dict)



