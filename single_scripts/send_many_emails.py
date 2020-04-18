# Send emails with Python

# SMTP: Simple Mail Transfer Protocol
# SSL: Secure Sockets Layer - creates a secure connection from the beginning
# TLS: Transport Layer Security - encryptes connection when need it

import csv
import smtplib
import ssl
from getpass import getpass

contacts_file = "../data/contact_details.csv"

message = """\
Subject: Hi there!
From: {sender}
To: {receiver}

Hi {name},
your email address is {receiver}.
This message is an automatic mail sent from Python!
"""

smtp_server = 'smtp.gmail.com'
port = 465

sender = input('Enter sender email: ')
password = getpass('Email password: ')

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print('You have successfully logged in!')
    with open(contacts_file) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            server.sendmail(sender, email, message.format(sender=sender,
                                                          receiver=email,
                                                          name=name)
                            )
            print(f'You just sent an email to {name}.')
