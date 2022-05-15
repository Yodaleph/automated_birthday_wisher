import smtplib
import random as rd
import pandas as pd
from datetime import datetime
##################### Importing the emails ######################
# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now().weekday()
file = pd.read_csv("birthdays.csv")
diction = dict(zip(file.loc[:, "name"].tolist(), file.loc[:, "email"].tolist()))
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if now == 0:
    for name in diction:
        with open("quotes.txt") as motivate:
            content = f"Subject:Hello {name}, \n\nIT'S MONDAY!!!!! \n{rd.choice(motivate.readlines())}"
# 4.Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as sender:
            sender.starttls()
            sender.login("yodaaleph@gmail.com","aboladedaniel")
            sender.sendmail(from_addr="yodaaleph@gmail.com",
                            to_addrs=diction[name],
                            msg = content)
