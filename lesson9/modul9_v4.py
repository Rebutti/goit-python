
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


@input_error
def parser(str_: str):
    listik = str_.split(' ')
    if listik[0].lower() in COMMANDS:
        command = listik[0].lower()
        del listik[0]
        return (command, listik)
    elif str_.lower() == 'show all':
        return(str_.lower(), [])


@input_error
def greetings(*args, **kwargs):
    return "Как я могу Вам помочь?"


CONTACTS = {}


@input_error
def new_contact(*args, **kwargs):
    information = args[0]
    name = information[0]
    phone = information[1]
    CONTACTS[name] = phone
    return f"{name} {phone} добавлен"


@input_error
def change_phone(*args, **kwargs):
    information = args[0]
    name = information[0]
    phone = information[1]
    if name in CONTACTS:
        CONTACTS[name] = phone
        return f"Номер для {name} изменен на {phone}"
    else:
        return "Такого пользователя не найдено"


@input_error
def show_all(*args, **kwargs):
    str_ = ''
    if CONTACTS == {}:
        return "Список пустой"
    else:
        for k, v in CONTACTS.items():
            str_ += k + " : "+v+'\n'
        return str_[:-1]


@input_error
def show_phone(*args, **kwargs):
    information = args[0]
    name = information[0]
    if name in CONTACTS:
        return f"Номер {name} : {CONTACTS[name]}"
    else:
        return "Такого контакта не найдено"


COMMANDS = {
    'hello': greetings,
    'add': new_contact,
    'show all': show_all,
    'change': change_phone,
    'phone': show_phone,
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
            break
        kort = parser(command)
        if kort == None:
            print(f"Команды {command} не найдено")
            continue
        handler = get_handler(kort[0])
        print(handler(kort[1]))


if __name__ == "__main__":
    main()
