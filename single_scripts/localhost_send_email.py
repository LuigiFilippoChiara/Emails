# Send emails with Python

# SMTP: Simple Mail Transfer Protocol
# SSL: Secure Sockets Layer - creates a secure connection from the beginning
# TLS: Transport Layer Security - encryptes connection when need it
# If you use a local server you do not need any encryption
# to run a localhost in Python run: python -m smtpd -c DebuggingServer -n localhost:1025

import smtplib

smtp_server = 'localhost'
port = 1025

sender = input('Enter sender email: ')
receiver = input('Enter receiver email: ')

message = f"""\
From: {sender}
To: {receiver}
Subject: Hi There!

This message was sent from Python! 
"""

try:
    server = smtplib.SMTP(smtp_server, port)
    server.sendmail(sender, receiver, message)
    print(f'You just sent an email to {receiver}')
except Exception as e:
    print(e)
    print('Remember to run a localhost. Ex: python -m smtpd -c DebuggingServer -n localhost:1025')
finally:
    server.quit()