# Send emails with Python

# SMTP: Simple Mail Transfer Protocol
# SSL: Secure Sockets Layer
# TLS: Transport Layer Security
# SSL creates a secure connection from the beginning, while TLS encryptes it when I need it
# HTML: Hypertext Markup Language
# MIME: Multipurpose Internet Mail Extensions. Today’s most common type of email (plain text + HTML)

import smtplib
import ssl
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re


def get_user_input_protocol():
    while True:
        protocol = input("Wich protocol do you want to use? (SSL, TLS, localhost): ").lower()
        if protocol in ('ssl', 'tls', 'localhost'):
            if protocol == 'localhost':
                print('Remember to run a localhost. Ex: python -m smtpd -c DebuggingServer -n localhost:1025')
            break
        else:
            print("Sorry, this is not a valid answer.")
            continue
    return protocol


def set_credentials(protocol):
    if protocol == 'localhost':
        # Note: if you use a local server you do not need any encryption
        smtp_server = 'localhost'
        port = 1025
        return smtp_server, port
    context = ssl.create_default_context()
    password = getpass('Email password: ')
    if protocol == 'ssl':
        smtp_server = 'smtp.gmail.com'
        port = 465
        return smtp_server, port, context, password
    elif protocol == 'tls':
        smtp_server = 'smtp.gmail.com'
        port = 587
        return smtp_server, port, context, password


def send_email_ssl(smtp_server, port, context, password,
                   sender_email, receiver_email, message):
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        print('You have successfully logged in!')
        server.sendmail(sender_email, receiver_email, message)
        print('You just sent an email.')


def send_email_tls(smtp_server, port, context, password,
                   sender_email, receiver_email, message):
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        # upgrade to encrypted connection
        server.starttls(context=context)
        server.ehlo()
        # now it's safe to login
        server.login(sender_email, password)
        print('You have successfully logged in!')
        server.sendmail(sender_email, receiver_email, message)
        print('You just sent an email.')
    except Exception as e:
        print(e)
    finally:
        server.quit()


def send_email_localhost(smtp_server, port, sender_email,
                         receiver_email, message):
    # Note: if you use a local server you do not need any encryption
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.sendmail(sender_email, receiver_email, message)
        print('You just sent an email.')
    except Exception as e:
        print(e)
    finally:
        server.quit()


def write_email(sender_email, receiver_email):
    message = MIMEMultipart("alternative")
    message["Subject"] = "MIME test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    This is the plain text version of the mail.
    """
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           <b>How are you?</b><br>
           This is the html version of the mail.
           At 
           <a href="https://www.google.com">Google</a> 
           you can find many interesting links!
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    return message

def insert_valid_email(who, domain=None):
    if domain:
        EMAIL_REGEX = re.compile(fr'^[a-z0-9_\.-]+@{domain}$')
    else:
        EMAIL_REGEX = re.compile(r'^[a-z0-9_\.-]+@[0-9a-z\.-]+\.[a-z\.]{2,6}$')

    while True:
        email = input(f'Enter {who} email: ')
        match = EMAIL_REGEX.fullmatch(email)
        if match:
            break
        if domain:
            print(f"Sorry, this is not a valid email. Remember to use the {domain} domain.")
        else:
            print(f"Sorry, this is not a valid email.")

    return match.group()


send_email_func_dict = {'ssl': send_email_ssl,
                        'tls': send_email_tls,
                        'localhost': send_email_localhost}
