# Send emails with Python

# SMTP: Simple Mail Transfer Protocol
# SSL: Secure Sockets Layer
# TLS: Transport Layer Security
# SSL creates a secure connection from the beginning, while TLS encryptes it when I need it
# HTML: Hypertext Markup Language
# MIME: Multipurpose Internet Mail Extensions. Today’s most common type of email (plain text + HTML)

import utils


def main():
    protocol = utils.get_user_input_protocol()

    # define credentials
    sender_email = input('Enter sender email: ')
    other_credentials = utils.set_credentials(protocol)
    receiver_email = input('Enter receiver email: ')

    # write email message
    message = utils.write_email(sender_email, receiver_email)

    # send an email with the right protocol
    utils.send_email_func_dict[protocol](*other_credentials, sender_email,
                                         receiver_email, message.as_string())


if __name__ == '__main__':
    main()
