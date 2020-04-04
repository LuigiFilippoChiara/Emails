# Send emails with Python

# SMTP: Simple Mail Transfer Protocol
# SSL: Secure Sockets Layer
# TLS: Transport Layer Security
# SSL creates a secure connection from the beginning, while TLS encryptes it when I need it
# HTML: Hypertext Markup Language
# MIME: Multipurpose Internet Mail Extensions. Today’s most common type of email (plain text + HTML)

import utils

# TODO: deal with multiple receiver mails
# TODO: send attachements (Adding Attachments Using the email Package)
# TODO: Sending Multiple Personalized Emails
# TODO: Yagmail


def main():
    # let user choose which protocol to use
    protocol = utils.get_user_input_protocol()

    # define credentials
    sender_email = utils.insert_valid_email(who='sender', domain='gmail.com')
    other_credentials = utils.set_credentials(protocol)
    receiver_email = utils.insert_valid_email(who='receiver')

    # write email message
    message = utils.write_email(sender_email, receiver_email)

    # send an email with the right protocol
    utils.send_email_func_dict[protocol](*other_credentials, sender_email,
                                         receiver_email, message.as_string())


if __name__ == '__main__':
    main()
