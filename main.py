from datetime import datetime, timedelta


def main():
    users = []
    with open('birthdays.txt', 'r') as file:
        for line in file:
            data = line.split()
            birthday = data[-1]
            try:
                birthday = datetime.strptime(birthday, '%m.%d.%Y')
            except ValueError:
                birthday = datetime.strptime(birthday, '%m.%d')
            users.append({'name': " ".join(data[:-1]), 'birthday': birthday})

    get_birthday_per_week(users)


def get_birthday_per_week(user_list):
    current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    lst = [[] for i in range(7)]
    for user in when_to_congratulate(user_list):
        day_to_birthday = user['when'] - current_date
        if 0 <= day_to_birthday.days <= 6:  # 7 next days
            lst[day_to_birthday.days].append(user['name'])
    for i in range(0, 7):
        if lst[i % 7]:  # don't print days without birthdays
            print((current_date + timedelta(days=i)).strftime("%A") + ": " + ", ".join(lst[i % 7]))


def when_to_congratulate(user_list):  # for each user finds a weekday in the current year when to congratulate them
    lst = []
    for user in user_list:
        birthday_day = user['birthday'].replace(year=datetime.now().year)  # set the current year
        if birthday_day.weekday() == 5:  # Saturday
            birthday_day += timedelta(days=2)
        elif birthday_day.weekday() == 6:  # Sunday
            birthday_day += timedelta(days=1)

        lst.append({'name': user['name'], 'when': birthday_day})
    return lst


if __name__ == '__main__':
    main()
