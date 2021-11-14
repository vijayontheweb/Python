import imaplib
import getpass
import email

mail_var = imaplib.IMAP4_SSL('imap.gmail.com')
email_addr = input('Email?')
# provide app password here
password = input('Password?')
mail_var.login(email_addr, password)
# ('OK', [b'(\\HasNoChildren) "/" "INBOX"', b'(\\HasChildren \\Noselect) "/" "[Gmail]"', b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"', b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"', b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"', b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"', b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"', b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"', b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Trash"'])
print(mail_var.list())
# ('OK', [b'50523'])
print(mail_var.select('inbox'))
typ, data = mail_var.search(None, 'SUBJECT "Hellow..."')
# OK
print(typ)
# [b'50516']
print(data)
# typ, data = mail_var.fetch(data[0],"(RFC822)")
result, email_data = mail_var.fetch(data[0], "(RFC822)")
print(result)
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
print(raw_email_string)
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        # Returns -> b'This is text!\r\n'
        print(body)
