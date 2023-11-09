#!/usr/bin/env/python3

import cgi
import smtplib
from email.mime.text import MIMEText

def send_email(email, comment):

    sender_email = '15077@coderacademy.edu.au'
    recipient_email = 'brett.russell2016@gmail.com'
    subject ='New Form Submission'
    body = f'email: {email}\ncomment: {comment}'

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, 'g0w8gssa')
        smtp_server.sendmail(sender_email, [recipient_email], message.as_string())
        smtp_server.quit()
        return True
    except Exception as e:
        print(f'Error sending email: {e}')
        return False

form = cgi.FieldStorage()

email = form.getvalue('email')
comment = form.getvalue('comment')

if not email or not comment:
    print("content-type: text/html\n")
    print("<html>")
    print("<body>")
    print("<p>Must submit a valid email address and enquiry.</p>")
    print("</body>")
    print("</html>")
else:
    if '@' not in email:
        print("content-type: text/html\n")
        print("<html>")
        print("<body>")
        print("<p>Invalid email address.</p>")
        print("</body>")
        print("</html>")
    else:
        if send_email(email, comment):
            print("content-type: text/html\n")
            print("<html>")
            print("<body>")
            print("<p>Thank you for your submission!</p>")
            print("</body>")
            print("</html>")
        else:
            print("content-type: text/html\n")
            print("<html>")
            print("<body>")
            print("<p>Error sending email. Please try again later.</p>")
            print("</body>")
            print("</html>")