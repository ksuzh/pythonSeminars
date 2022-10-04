def show_menu() -> int:
    print("\n Choose action:\n"
          "1. Show whole phonebook\n"
          "2. Find user by surname\n"
          "3. Find user by phone number\n"
          "4. Add user to phonebook\n"
          "5. Finish work")
    choice = int(input())
    return choice


def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s+= f'{v}: {k}\n'
        print(s)

def get_name() -> str:
    return input('Input the last name: ')

def get_number() -> str:
    return input('Input the phone number: ')

def get_user() -> str:
    last_name = input('Input the last name: ')
    first_name = input('Input the name: ')
    phone_number = input('Input the phone number: ')
    return f'{last_name}, {first_name}, {phone_number}'

    
    


