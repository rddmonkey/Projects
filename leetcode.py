import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from email import message

from_addr = 'rddmonkey@gmail.com'
to_addr = 'richd_chang@hotmail.com'
subject = 'I just sent this attachment from Python!'
content = 'How neat is that?'

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

filename = "test.txt"

with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
    msg.attach(part)

msg.attach(part)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(from_addr,"password")
server.send_message(msg, from_addr=from_addr, to_addrs=to_addr)
