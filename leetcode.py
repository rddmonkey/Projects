
import smtplib

from email import message

from_addr = "rddmonkey@gmail.com"
to_addr = "richd_chang@hotmail.com"

subject = "I just sent this from Python!"
body = "this is so cool"

msg = message.Message()

msg.add_header('from', from_addr)
msg.add_header("to",to_addr)
msg.add_header("subject",subject)
msg.set_payload(body)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login(from_addr, "password")

server.send_message(msg, from_addr=from_addr, to_addrs = to_addr)
exit()