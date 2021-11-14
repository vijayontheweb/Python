import smtplib
import getpass

# 587 - TLS connection meaning its encrypted. Port 465 is SSL
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
# (250, b'smtp.gmail.com at your service, [183.82.28.15]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
print(smtp_object.ehlo())
# (220, b'2.0.0 Ready to start TLS')
print(smtp_object.starttls())
# demonstrating masked input
plain_text_password = input('What is your password?')
masked_password = getpass.getpass('What is your (masked)password?')
email = getpass.getpass('Email?')
# provide app password here
password = getpass.getpass('Password?')
# (235, b'2.7.0 Accepted')
print(smtp_object.login(email, password))
from_address = email
to_address = email
subject = input('enter mail subject')
message = input('enter message')
msg = 'Subject: '+subject+'\n'+message
smtp_object.send(msg)
smtp_object.quit()
