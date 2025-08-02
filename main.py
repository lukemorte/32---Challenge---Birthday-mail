##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import random
import smtplib
from email.message import EmailMessage
import datetime as dt
import os


# const & vars

MAIL_HOST = "smtp.seznam.cz"
MAIL_USER = "py_test@seznam.cz"
MAIL_PASSWORD = "jjz!AtuDYiN#46@"

BIRTHDATES_FILE = "birthdays.csv"
LETTER_TAMPLATES_DIR = "./letter_templates/"

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


def get_named_random_letter(user):
    all_letter_files = [f for f in os.listdir("./letter_templates")
                        if f.startswith("letter_") and f.endswith(".txt")]
    random_letter = random.choice(all_letter_files)
    print(LETTER_TAMPLATES_DIR + random_letter)

    with open(LETTER_TAMPLATES_DIR + random_letter) as file:
        letter = file.read()
        letter = letter.replace("[NAME]", user["name"])

    return letter


def send_mail(user, letter):
    with smtplib.SMTP(MAIL_HOST) as connection:
        connection.starttls()
        connection.login(user=MAIL_USER, password=MAIL_PASSWORD)

        msg = EmailMessage()
        msg.set_content(letter)
        msg["Subject"] = f"Happy birthday {user["name"]}"
        msg["From"] = MAIL_USER
        msg["To"] = user["email"]

        connection.send_message(msg)


# code


birth_data = get_people_data()
birth_data_match_today = get_people_data_match_today(birth_data)

if birth_data_match_today:
    for user in birth_data_match_today:
        letter = get_named_random_letter(user)
        send_mail(user, letter)
