#!python3

import requests
from bs4 import BeautifulSoup
import smtplib
import time
import codecs
import re

# Fill in URL of product you want to scrape
# User-agent address can be found by googling "My user-agent"
URL = "https://www.netonnet.no/art/gaming/spillogkonsoll/nintendo/nintendo-spill/nintendo-super-mario-3d-all-stars/1014400.15691/"
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}


# Use F12 on the websites you want to find the title and price. They usually have an id or a class to signalise them.
def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(attrs={"subTitle big"}).get_text()
    price = soup.find(attrs={"price-big"}).get_text()
    price = price.strip()
    converted_price = int(price[:3])
    print (converted_price)



    # Issue for converted price - Not the case here, because there were no spaces in the price. As soon as there
    # are 4 digits and above, I don't know how to deal with it. Most likely, regex could fix it.

    # Change this number for any given price you want.
    if converted_price < 700:
        send_mail()

    print(title),
    print(converted_price)


# If you are using gmail, this information doesn't have to change.
def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # The password is a self generated one. You can get a one-time password by activating 2-step-verification
    # and including a password exclusively for this.
    server.login("tordar.tommervik@gmail.com", "zxmvjsaizzsrjzzd")

    subject = "Prisen for Mario har gått ned på NetOnNet:"
    body = ("Check this link: " + URL)

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "tordar.tommervik@gmail.com",
        "tordar.tommervik@gmail.com",
        msg.encode()
    )
    print("Email has been sent!")
    server.quit()


# Here you can add a while loop and a time.sleep() function to make it repeat itself in given intervals
while True:
    #time.sleep(60)
    check_price()
    break
