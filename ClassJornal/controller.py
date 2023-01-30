import view
import model


def start():

    model.set_class(view.input_class())
    while model.chekc_subject() == True:
        model.set_subject(view.input_subject())
        if model.chekc_subject() == True:
            print(view.wrong_subject())

    model.open_file()
    view.table_columns()

    student = ''
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)

        student = view.who_answer()
        while model.chekc_student(student) == True:
            print(view.wrong_student())
            student = view.who_answer()


        if student == 'exit':
            break
        mark = int(view.what_mark())
        model.student_mark(student, mark)
    model.save_file()
