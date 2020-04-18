# Emails with Python
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](/LICENSE)

Learning how to send emails with Python.  
Note: if you have a <em>Gmail</em> account, the easiest solution is to use [**yagmail**](https://yagmail.readthedocs.io/en/latest/).

## Some theory

In this project automatic emails are sent with <b>SMTP</b> (Simple Mail Transfer Protocol), the most common communication protocol for electronic mail transmission.

Transport Layer Security (<b>TLS</b>), and its now-deprecated predecessor, Secure Sockets Layer (<b>SSL</b>), are cryptographic protocols designed to provide communications security over a computer network. <b>SSL</b> creates a secure connection from the beginning, while <b>TLS</b> starts with an unsecure connection and encryptes it later.

Multipurpose Internet Mail Extensions (**MIME**) is an Internet standard that extends the format of email messages to support text in character sets other than ASCII, as well as attachments of audio, video, images, and application programs. Nowadays this is the most common email type. It usually contains both a plain text and html versions of the same message.

## Project description

The scripts of this project allow you to send automatic emails from/to your localhost or connecting to a <em>Gmail</em> account.  

1. Sending email from and to your localhost is easier, you don't need to create a real email address and your computer is sending a message to itself. Just remember to run
```
python -m smtpd -c DebuggingServer -n localhost:1025
```
in a terminal window for your localhost to receive these emails. The received emails will be displayed in your terminal. Since everything is happening locally, there is no need to encrypt any connection. To use your local host to need the server name ('localhost') and a port number (1025 in this case).

2. To start sending real emails, it is suggested to use a <em>Gmail</em> account explicitely created for sending automatic emails, with modified security restrictions (see <a href="https://realpython.com/python-send-email/" target="_blank" rel="noopener nofollow noreferrer">Sending Emails With Python</a> for more detail). The scripts will then ask for your email address and password to automatically login to your email account and send emails from there. In this case the connection must be encrypted for security reasons, either with SSL or TLS. To connect to your <em>Gmail</em> account you need the server name ('smtp.gmail.com') and the port number (465 for SSL and 587 for TLS).

3. Finally, **yagmail** is a GMAIL/SMTP client that aims to make it as simple as possible to send automatic emails with <em>Gmail</em>, and it greatly simplifies the process through a friendly API. **yagmail** takes care of security and passwords for you.


## Getting started

First of all, `fork` this repo and then `clone` your fork to have a local copy. All the data comes with the repo.

To use **yagmail** you first need to install it. You can create this project's environment with

```
conda env create -f emails_with_python.yml
```
and then activate it with

```
conda activate emails_with_python
```
  
Alternatively, you can install **yagmail** directly by running

```
pip install yagmail[all]
```

in a terminal. It is recommended to install it with the `[all]` specification, in order to install the **keyring** library too.

## Scripts description

The main program of this project is `send_email.py`, which is an interactive script that allows you to send a **MIME** email.  
This email contains both a HTML and a plain text version of a message, and an optional pdf attachment.
You can choose to send the email with your localhost or with a <em>Gmail</em> account (with SSL or TLS encryption). Moreover, a *RegEx* check of the emails addresses is performed during execution. Run the script with

```
python send_email.py
```
and enter the required information.

Finally, the folder `single_scripts` contains some useful scripts:

1. `localhost_send_email.py` sends a single plain text email from/to your **localhost**.
2. `ssl_send_email.py` sends a single plain text email from your <em>Gmail</em> account with **SSL** encryption.
3. `tls_send_email.py` sends a single plain text email from your <em>Gmail</em> account with **TLS** encryption.
4. `yagmail_send_email.py` sends a plain text single email with a pdf attachment from your <em>Gmail</em> account, using **yagmail**.
5. `send_many_emails.py` sends personalised automatic plain text emails in a for loop, taking the contact details from `data/contact_details.csv`. The connection is encrypted with **SSL**.

## Acknowledgements

Most of this content was inspired by *Sending Emails With Python* from [realpython.com](https://realpython.com/python-send-email).

## License

This project is licensed under the MIT License. Use it as you wish.
