from dataclasses import dataclass



def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].value():
                s += v + ','
            fout.write(f'{s[:1]}\n')


def read_csv(filename: str) -> list:
    data =[]
    fields = ["Surname", "Name", "Phone_number"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data


def find_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Last name") == last_name:
            return el.get("Phone_number")
    return "No user"

def find_number(data: list, phone_number: str) -> str:
    for el in data:
        if el.get("Phone_number") == phone_number:
            return f'el.get{"Surname"}, {"Name"}'
    return "No user"

def add_user(data:list, user_data: str):
    fields = ["Surname", "Name", "Phone_number"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)
