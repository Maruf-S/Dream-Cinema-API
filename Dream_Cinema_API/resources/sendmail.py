import smtplib, ssl
from smtplib import SMTP
from email.mime.text import MIMEText

def sendMailToClient(ticket, userEmail):
    port = 587
    smtp_server = "smtp.gmail.com"
    login = 'c3418a1b389673'
    password = 'dreamcinema@gmail.com'
    message = "<h3>below is your ticket number</h3>\
            <ul><li>Ticket Number:<strong> {}</strong></li>".format(ticket.ticket_id)

    sender_email = 'dreamcinemamtma@gmail.com'
    receiver_email = userEmail
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'DreamCinemaTicket'
    msg['From']=sender_email
    msg['To']=receiver_email
    print("herewew")


    # context = ssl.create_default_context()
    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.ehlo()  # Can be omitted
    #     server.starttls(context=context)
    #     server.ehlo()  # Can be omitted
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, msg.as_string())


    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL('smtp.gmail.com', port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email,password)
    server.sendmail(
    sender_email, receiver_email, msg.as_string())
    server.quit()
    

