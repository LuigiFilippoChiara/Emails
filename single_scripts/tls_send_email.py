# Send emails with Python

# SMTP: Simple Mail Transfer Protocol
# SSL: Secure Sockets Layer - creates a secure connection from the beginning
# TLS: Transport Layer Security - encryptes connection when need it

import ssl
import smtplib
from getpass import getpass

smtp_server = 'smtp.gmail.com'
port = 587

sender = input('Enter sender email: ')
password = getpass('Email password: ')
receiver = input('Enter receiver email: ')

message = f"""\
From: {sender}
To: {receiver}
Subject: Hi There!

This message was sent from Python! 
"""

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    # upgrade to encrypted connection
    server.starttls(context=context)
    server.ehlo()
    # now it's safe to login
    server.login(sender, password)
    print('You have successfully logged in!')
    server.sendmail(sender, receiver, message)
    print(f'You just sent an email to {receiver}')
except Exception as e:
    print(e)
finally:
    server.quit()