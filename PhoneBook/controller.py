import model
import view
model.read_file('data.txt')

user_input = view.main_menu()

def command_handler(user_input: int):
    match user_input:
        case 1: view.show_all(model.db_list)

command_handler((user_input))