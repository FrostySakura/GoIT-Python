from datetime import datetime, date, timedelta
import calendar


def find_start_end_next_week():
    today_date = date.today()
    delta_1 = timedelta(days=(5 - today_date.weekday()))
    start_date = today_date + delta_1
    last_date = start_date + timedelta(days=6)
    return start_date, last_date,


# def find_next_week():
#     today_date = date.today()
#     delta_1 = timedelta(days=(5 - today_date.weekday()))
#     start_date = today_date + delta_1
#     return [start_date + timedelta(i) for i in range(7)]


def pre_print_dict(data: dict):
    result = ''
    for key, value in data.items():
        value = ', '.join(value)
        result += f'{calendar.day_name[key]} : {value}\n'
    return result



def find_next_week_birthdays(users, start_date, last_date):
    """

    :param users: list of dict where key : users name (str), value : date of birth (datetime)
    :param start_date: (datetime) - saturday - start iteration with
    :param last_date: (datetime) - friday - stop iteration with
    :return: list of dict where: key : (int) weekday; value : list of users names (str)
    """
    result = []
    while start_date <= last_date:
        new_dict = {}
        who_birthday = []
        for user_dict in users:
            for name, birthday_date in user_dict.items():
                if birthday_date.month == start_date.month and birthday_date.day == start_date.day:
                    week_day = start_date.weekday()
                    who_birthday.append(name)
                    new_dict[week_day] = who_birthday
        if new_dict:
            result.append(new_dict)

        start_date += timedelta(1)

    return result


def transform_list_to_dict(data):
    result = {}
    value_1 = []
    for d_item in data:
        for key, value in d_item.items():
            if key == 5 or key == 6 or key == 0:
                a = value
                value_1 += a
                result[0] = value_1
            else:
                result[key] = value
    return result


day_1 = datetime(year=1990, month=9, day=7)
day_2 = datetime(year=1989, month=8, day=14)
day_3 = datetime(year=2000, month=8, day=15)
day_4 = datetime(year=2009, month=8, day=20)
day_5 = datetime(year=2001, month=8, day=22)
day_6 = datetime(year=1999, month=8, day=15)
day_7 = datetime(year=2001, month=8, day=17)
day_8 = datetime(year=2010, month=8, day=18)
day_9 = datetime(year=2002, month=8, day=21)
day_10 = datetime(year=1993, month=8, day=16)


A = [{'U_1': day_1},
     {'U_2': day_2},
     {'U_3': day_3},
     {'U_4': day_4},
     {'U_5': day_5},
     {'U_6': day_6},
     {'U_7': day_7},
     {'U_8': day_8},
     {'U_9': day_9},
     {'U_10': day_10},]
        

n, m = find_start_end_next_week()
r = find_next_week_birthdays(A, n, m)
q = transform_list_to_dict(r)
print(pre_print_dict(q))

   

