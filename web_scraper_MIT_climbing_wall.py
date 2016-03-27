#from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
from datetime import date
#import csv

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

url = "http://scripts.mit.edu/~mitoc/wall/"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html.parser")



def is_wall_open(): # just tells if "open" is lit up
    # target open with selector
    status_element = soup.select("#status .open .name")[0]['class']
    # search for class find or findall (BS4) find atter
    # specify what class to return (check type), check contents of string
    # returns <span class="name dim">open</span>
    #status_element.attrs
    #class_status_element = status_element['class']
    #print(class_status_element) # 'u' means unicode, not string
    #return class_status_element
    # should I escape the u or just love that it's there?
    # oh, it's a list.  thank god.
    # use in for Boolean
    return "dim" not in status_element


def when_next_open(): # looks to see when is next open
    pass

def email_the_crew(): # composes and sends email
    # fill in email things: list address, subject, text
    # call filler fcn that randomizes email text for optimal fun
    # send
    recipents = ["vehanus@gmail.com, cestdiego@gmail.com"]
    subject = "THE WALL IS OPEN BITCHESSSSSS"
    text = "Wall is open from now until ..."

    SMTP_server = "smtp.gmail.com"
    SMTP_port = 587
    SMTP_username = "veronica.codes.good@gmail.com"
    SMTP_password = "veronicaisgreat"
    date_format = "%d/%m/%y"

    msg = MIMEText(text)
    msg['Subject'] = subject + " %s" % (date.today().strftime(date_format))
    msg['From'] = "veronica.codes.good@gmail.com"
    msg['To'] = ", ".join(recipents)
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

# maybe use smtplib (Darius' suggestion)

# flag w/ boolean
# so if was open the last minute, don't send the email because you know it has already been sent
# but what about back to back hours of openness?
# could have var that is empty or contains closing time. can check at one min after closing if it is open again

wall_open = not is_wall_open()
email_the_crew()


def main():
    pass
    # call is wall open
    # if open, call email the crew
