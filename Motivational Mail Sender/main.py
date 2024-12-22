import smtplib
import datetime as dt
import random

# TODO: You have to create an app password for the email and use it and also keep your 2-Step Verification ON
MY_EMAIL = "sidharthmk009@gmail.com"
PASSWORD = "eavixmenuyfseqsf"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt", encoding="utf8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # MAKES CONNECTION SECURE
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="hkbimal@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n"f"{quote}".encode("utf8"))

# year = now.year
# month = now.month
#
# date_of_birth = dt.datetime(year=1994, month=6, day=14, hour=4, minute=20)
# print(date_of_birth)
