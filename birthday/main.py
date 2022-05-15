import smtplib
import random
import pandas as pd
from datetime import datetime
##################### Extra Hard Starting Project ######################
# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
today =(now.month, now.day)
file = pd.read_csv("birthdays.csv")
data = {(row.month, row.day):row for (index, row) in file.iterrows()}
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today in data:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as birthday_wish:
        content = birthday_wish.read().replace("[NAME]", data[today]["name"])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as sender:
        sender.starttls()
        sender.login("yodaaleph@gmail.com", "aboladedaniel")
        sender.sendmail(from_addr = "yodaaleph@gmail.com",
                        to_addrs = data[today].email,
                        msg = content)

