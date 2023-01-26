import model
import view




def command_handler(user_input: int):
    match user_input:
        case 1: view.show_all(model.db_list)
        case 2: model.read_file('data.txt')
        case 3: view.save_book(model.db_list)
        case 4: model.db_list.append(view.create_contact())
        case 5: view.cgange_contact(model.db_list)
        case 6: view.delete_contact(model.db_list)
        case 7: view.search_contact(model.db_list,view.write_surname())
        case 8: view.exit_programm()


while True:

    user_input = view.main_menu()
    command_handler((user_input))







