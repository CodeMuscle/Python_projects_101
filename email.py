import smtplib


SENDER_EMAIL = 'bulldogsrescue@gmail.com'
SENDER_PASSWORD = 'jgg20000'

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n {}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)

        