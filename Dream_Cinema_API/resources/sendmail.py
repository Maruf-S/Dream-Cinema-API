import smtplib
from email.mime.text import MIMEText

def sendMailToTutor(ticket_Id, tutorEmail):
    port = 2525
    smtp_sever = 'smtp.mailtrap.io'
    login = '3aace52c5332a2'
    password = '6397b758c896a4'
    message = """ 
    <!DOCTYPE html>
<html>
<body>

<h3>Ticket</h3>

<figure>
  <img src='https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={}' alt='Ticket'>
  <figcaption>Movie Ticket for Aqua Man</figcaption>
</figure>

</body>
</html>
    """.format(ticket_Id)
    sender_email = 'DreamCinema@Ticket.com'
    reciever_email = tutorEmail
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Ticket confirmation'
    msg['From']=sender_email
    msg['To']=reciever_email

    with smtplib.SMTP(smtp_sever, port) as server:
        server.login(login, password)
        print(server.sendmail(sender_email, reciever_email, msg.as_string()))


