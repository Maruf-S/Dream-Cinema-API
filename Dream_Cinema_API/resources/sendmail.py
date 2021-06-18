import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText

def sendMailToClient(ticket, userEmail):
    port = 587
    smtp_sever = 'smtp.mailtrap.io'
    login = 'c3418a1b389673'
    password = '04b7ad9099e1bc'
    message = "<h3>below is your ticket number</h3>\
            <ul><li>Ticket Number:<strong> {}</strong></li>".format(ticket.ticket_id)

    sender_email = 'dreamcinemamtma@gmail.com'
    reciever_email = userEmail
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'DreamCinemaTicket'
    msg['From']=sender_email
    msg['To']=reciever_email

    with smtplib.SMTP(smtp_sever, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())

