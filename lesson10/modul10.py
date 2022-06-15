from collections import UserDict


class Field():
    pass


class AdressBook(UserDict):
    def add_record(self, rec):
        self.data[rec.name] = rec


class Name(Field):
    name = ''

    def __init__(self, name) -> None:
        self.name = name


class Phone(Field):
    phone = ''

    def __init__(self, phone=None) -> None:
        self.phone = phone


class Record():
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phone = phone

    def change2_phone(self, phone):
        self.phone = phone

    def delete(self):
        self.phone = '-'


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except IndexError:
            return "Вы ввели не полные данные"
        except TypeError:
            return "Вы ввели что-то лишнее"
        except KeyError:
            return "Вы ввели не полные данные. Попробуйте снова"
        return result
    return inner


@ input_error
def parser(str_: str):
    listik = str_.split(' ')
    if str_.lower() == 'show all':
        return(str_.lower(), [])
    elif listik[0].lower() in COMMANDS:
        command = listik[0].lower()
        del listik[0]
        return (command, listik)


@ input_error
def greetings(*args, **kwargs):
    return "Как я могу Вам помочь?"


# CONTACTS = {}
CONTACTS = AdressBook()


@ input_error
def new_contact(*args, **kwargs):
    information = args[0]
    name = Name(information[0])
    try:
        phone = Phone(information[1])
    except:
        phone = Phone('-')
    rec = Record(name, phone)
    CONTACTS.add_record(rec)
    return f"{name.name} {phone.phone} добавлен"


# @ input_error
def change_phone(*args, **kwargs):
    information = args[0]
    name = Name(information[0])
    phone = Phone(information[1])
    rec = Record(name, phone)
    for k, v in CONTACTS.items():
        if k.name == name.name:
            CONTACTS[k].change2_phone(phone)
            return "Номер изменен"
    return "Такого пользователя не найдено"


@ input_error
def show_all(*args, **kwargs):
    str_ = ''
    if CONTACTS == {}:
        return "Список пустой"
    else:
        for k, v in CONTACTS.items():
            try:
                str_ += str(v.name.name) + " : " + str(v.phone.phone) + '\n'
            except AttributeError:
                str_ += str(v.name.name) + " : " + str(v.phone) + '\n'
        return str_[:-1]


@ input_error
def delete_contact(*args, **kwargs):
    information = args[0]
    name = Name(information[0])
    for k, v in CONTACTS.items():
        if k.name == name.name:
            CONTACTS[k].delete()
            return "Пользователь удален"
    return "Такого пользователя не найдено"


@ input_error
def show_phone(*args, **kwargs):
    information = args[0]
    str_ = ''
    if CONTACTS == {}:
        return "Список пустой"
    else:
        for k, v in CONTACTS.items():
            if k.name == information[0]:
                return f"Номер {k.name} : {CONTACTS[k].phone.phone}"
        return "Такого контакта не найдено"


COMMANDS = {
    'hello': greetings,
    'add': new_contact,
    'show all': show_all,
    'change': change_phone,
    'phone': show_phone,
    'delete': delete_contact,


}


def get_handler(operator):
    return COMMANDS[operator]


def main():
    flag = 1
    exit_words = ["good bye", "close", "exit", '.']
    kort = None  # будующий кортеж где первый эллемент - команда, воторой - данные
    while flag != 0:
        command = input("Введите команду: ")
        if command.lower() in exit_words:
            print("Bye")
            break
        kort = parser(command)
        if kort == None:
            print(f"Команды {command} не найдено")
            continue
        handler = get_handler(kort[0])
        print(handler(kort[1]))
        # print(CONTACTS)


if __name__ == "__main__":
    main()
