# Send emails with Python

# SMTP: Simple Mail Transfer Protocol
# SSL: Secure Sockets Layer - creates a secure connection from the beginning
# TLS: Transport Layer Security - encryptes connection when need it
# HTML: Hypertext Markup Language
# MIME: Multipurpose Internet Mail Extensions. Most common type (text + HTML)

import utils


def main():
    # let user choose which protocol to use
    protocol = utils.get_user_input_protocol()

    # define credentials
    sender_email = utils.insert_valid_email(who='sender', domain='gmail.com')
    other_credentials = utils.set_credentials(protocol)
    receiver_email = utils.insert_valid_email(who='receiver')

    # write email message
    message = utils.write_email(sender_email, receiver_email,
                                attachment_filename='data/dog.pdf')

    # send an email with the right protocol
    utils.send_email_func_dict[protocol](*other_credentials, sender_email,
                                         receiver_email, message)


if __name__ == '__main__':
    main()
