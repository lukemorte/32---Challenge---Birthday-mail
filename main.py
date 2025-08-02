##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import random
import smtplib


# const & vars

BIRTHDATES_FILE = "birthdays.csv"

birth_data = {}


def get_people_data():
    try:
        data = pandas.read_csv(BIRTHDATES_FILE)
        return pandas.DataFrame(data).to_dict("records")

    except FileNotFoundError:
        print("File not found.")

    else:
        print()


birth_data = get_people_data()

if birth_data:
    for n in birth_data:
        print(n)
