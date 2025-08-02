##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import random
import smtplib
import datetime as dt


# const & vars

BIRTHDATES_FILE = "birthdays.csv"

birth_data = None
birth_data_match_today = None


def get_people_data():
    try:
        data = pandas.read_csv(BIRTHDATES_FILE)
        return pandas.DataFrame(data).to_dict("records")

    except FileNotFoundError:
        print("File not found.")


def get_people_data_match_today(data):
    now = dt.datetime.now()
    arr = []

    for user in data:
        user_date = dt.datetime(year=user["year"], month=user["month"], day=user["day"])
        if user_date.year == now.year and user_date.month == now.month and user_date.day == now.day:
            arr.append(user)

    return arr


def prepare_random_mail(user):
    pass


# code


birth_data = get_people_data()
birth_data_match_today = get_people_data_match_today(birth_data)

if birth_data_match_today:
    for user in birth_data_match_today:
        prepare_random_mail(user)
