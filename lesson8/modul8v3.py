from datetime import date, datetime, timedelta
from collections import defaultdict
"""
Программа выводит людей у кого будет день рождения в ближайшие 7 дней, не включая день, в который была запущена программа
"""


def get_birthdays_per_week(users: list):
    list_ = []
    #today = datetime(year=2022, month=12, day=30)
    today = datetime.now()
    today_in_week = today + timedelta(days=7)
    this_year_in_days = datetime.toordinal(
        datetime(year=today.year, month=1, day=1))
    for i in users:
        str_ = i["birthday"]
        if i["birthday"][5:7] == '01':
            i["birthday"] = str(today.year+1) + str_[4:]
        else:
            i["birthday"] = str(today.year) + str_[4:]
        i["birthday"] = datetime.strptime(i['birthday'], '%Y-%m-%d')
        i["birthday"] = datetime.toordinal(i["birthday"]) - this_year_in_days
    # print(users)
    today = datetime.toordinal(today) - this_year_in_days
    today_in_week = datetime.toordinal(today_in_week) - this_year_in_days
    #print(today, today_in_week)

    for user in users:
        if int(user["birthday"]) > int(today) and int(user["birthday"]) < int(today_in_week):
            # print(user["name"])
            user["birthday"] += this_year_in_days
            user["birthday"] = date.fromordinal(user["birthday"])
            user["birthday"] = user["birthday"].weekday()
            list_.append(user)

    weekdays = defaultdict(list)
    for i in list_:
        weekday = i['birthday']
        weekdays[weekday].append(i['name'])
    dict_ = {
        "Monday": None,
        "Tuesday": None,
        "Wednesday": None,
        "Thursday": None,
        "Friday": None
    }
    for k, v in weekdays.items():
        str_ = ', '.join(v)
        if k == 4:
            dict_["Friday"] = str_
        elif k == 1:
            dict_["Tuesday"] = str_
        elif k == 2:
            dict_["Wednesday"] = str_
        elif k == 3:
            dict_["Thursday"] = str_
        else:
            dict_["Monday"] = str_
    for k, v in dict_.items():
        if(v != None):
            print(f"{k}: {v}")


if __name__ == "__main__":
    users = [
        {
            "name": "Alex",
            "birthday": "1988-05-16"
        },
        {
            "name": "Nina",
            "birthday": "1999-05-18"
        },
        {
            "name": "Bill",
            "birthday": "1988-05-20"
        },
        {
            "name": "Oleg",
            "birthday": "1988-05-14"
        },
        {
            "name": "Alla",
            "birthday": "1988-05-17"
        },
        {
            "name": "Nikita",
            "birthday": "1988-05-22"
        },
        {
            "name": "Mike",
            "birthday": "1988-05-20"
        },
        {
            "name": "Olya",
            "birthday": "1988-12-31"
        },
        {
            "name": "Dima",
            "birthday": "1989-01-04"
        },
        {
            "name": "Vika",
            "birthday": "2002-05-22"
        },
        {
            "name": "Kirill",
            "birthday": "1989-01-09"
        }
    ]
    get_birthdays_per_week(users)
