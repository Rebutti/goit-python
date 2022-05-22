def greetings():
    return "How can I help you?"


contacts = {}


def new_contact(inform: list):
    contacts[inform[0]] = inform[1]


def show_all():
    str_ = ''
    if contacts == {}:
        return "список пустой"
    for k, v in contacts.items():
        str_ = str_+f'Имя {k}, номер: {v}\n'

    return str_[:-1]


def change_phone(inform: list):
    if inform[0] in contacts:
        contacts[inform[0]] = inform[1]
    else:
        raise KeyError("такого имени не найдено")


def show_phone(inform: str):
    return f"номер: {contacts[inform]}"


COMMANDS = {
    'hello': greetings,
    'add': new_contact,
    'show all': show_all,
    'change': change_phone,
    'phone': show_phone,
    # 'change': change_phone,
}


def main():
    exit_words = ["good bye", "close", "exit", '.']
    information = []
    while True:
        command = input("Введите команду: ")
        if command in exit_words:
            print("Bye!")
            break
        else:
            if command in COMMANDS:
                print(COMMANDS[command]())
            else:
                command = command.split(" ")
                if len(command) == 1:
                    for k, v in COMMANDS.items():
                        if k == command[0].lower():
                            print(v())
                elif len(command) == 2:
                    for k, v in COMMANDS.items():
                        if k == command[0].lower():
                            print(v(command[1]))
                else:
                    for k, v in COMMANDS.items():
                        if k == command[0].lower():
                            inform = []
                            inform.append(command[1])
                            inform.append(command[2])
                            try:
                                v(inform)
                            except KeyError:
                                print('Вы ввели не корректные данные')

        # print(contacts)


if __name__ == "__main__":
    main()
