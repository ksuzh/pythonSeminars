from secrets import choice
from view import show_menu, print_result, get_name, get_number, get_user
from model import write_csv, read_csv, find_name, find_number, add_user


def processing_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while choice !=5:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_name()
            print(find_name(phone_book, name))
        elif choice == 3:
            number = get_number()
            print(find_number(phone_book, number))
        elif choice == 4:
            user_data = get_user
            add_user(phone_book, user_data)
            write_csv('book.csv')
        choice = show_menu()