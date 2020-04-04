# Send emails with Python

# SMTP: Simple Mail Transfer Protocol
# SSL: Secure Sockets Layer
# TLS: Transport Layer Security
# SSL creates a secure connection from the beginning, while TLS encryptes it when I need it
# If you use a local server you do not need any encryption
# to run a localhost in Python run: python -m smtpd -c DebuggingServer -n localhost:1025

import smtplib

smtp_server = 'localhost'
port = 1025

sender = input('Input sender email: ')
receiver = input('Input receiver email: ')

print('Remember to run a localhost. Ex: python -m smtpd -c DebuggingServer -n localhost:1025')

message = f"""\
From: {sender}
To: {receiver}
Subject: Hi There!

This message was sent from Python! 
"""

try:
    server = smtplib.SMTP(smtp_server, port)
    server.sendmail(sender, receiver, message)
    print('You just sent an email.')
except Exception as e:
    print(e)
finally:
    server.quit()