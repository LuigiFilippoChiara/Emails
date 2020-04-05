# Yagmail is designed to work specifically with Gmail, and it greatly
# simplifies the process of sending emails through a friendly API

import yagmail

sender = input('Enter sender email: ')
receiver = input('Enter receiver email: ')

subject = "Yagmail test with attachment"
body = "Hello there from Yagmail"
attachment_filename = "../data/dog.pdf"

yag = yagmail.SMTP(sender)
yag.send(
    to=receiver,
    subject=subject,
    contents=body,
    attachments=attachment_filename,
)