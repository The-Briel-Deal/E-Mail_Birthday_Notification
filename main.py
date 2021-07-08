# ----- IMPORTING MODULES ------ #
import pandas
import datetime
import random
import smtplib
import email.message

# ----- DEFINING VARIABLES ------ #
DAY = datetime.datetime.now().day
MONTH = datetime.datetime.now().month
BIRTHDAYS = pandas.read_csv('birthdays.csv')

#  !!! Write mailing list separated by ', ' !!!
MAILING_LIST = ""

#  Credentials
my_email = ""
password = ""

# ----- CREATE LETTER ------ #
for _ in range(BIRTHDAYS.shape[0]):  # Go through every single row
    if BIRTHDAYS.loc[_, "month"] == MONTH and BIRTHDAYS.loc[_, "day"] == DAY:  # And check if any are equivalent
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:  # Then pull a random letter
            made_letter = letter.read().replace("[NAME]", BIRTHDAYS.loc[_, "name"], 1)  # And replace with their name

# ----- COMPOSING E-MAIL ----- #
MESSAGE = email.message.EmailMessage()

MESSAGE['Subject'] = 'Happy Birthday!!!'
MESSAGE['From'] = ''
MESSAGE['To'] = MAILING_LIST
MESSAGE.set_content(made_letter)

# ----- INITIALIZING CONNECTION ----- #
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

# ----- SEND E-MAIL ----- #
connection.send_message(MESSAGE)
connection.close()
