import smtplib
import datetime as dt
import random
my_email = "yourmail"
my_pass = "yourmailapppassword"
with smtplib.SMTP("smtp.gmail.com") as connection:
        with open("quotes.txt","r") as quote_file:
            all_quotes= quote_file.readlines()
            random_quote = random.choice(all_quotes)
            dob = dt.datetime(day=4, year=2023, month=1, hour=18, minute=45)
            cur = dt.datetime.now()
            cur_time = dt.datetime(year=cur.year, day=cur.day, month=cur.month, hour=cur.hour, minute=cur.minute)
            if dob == cur_time:

                connection.starttls()
                connection.login(user = my_email, password=my_pass)
                connection.sendmail(from_addr=my_email, to_addrs="sendermail", msg=f"Subject: Hey "
                                                                                                       f"there\n\nMy "
                                                                                                       f"name is"
                                                                                                       f"your name "
                                                                                                       f"Happy Birthday🎂"
                                                                                                       f"\n\n"
                                                                                                       f"{random_quote}")
                print("Message sent")

