import smtplib

sender_email = input("Enter the sender email address : ")
password = input("Enter the sender email password : ")
to_email = input("Enter the receiver email address : ")
message = input("Enter the message to receiver : ")


def sendEmail(sender_email, password, to_email, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, to_email, message)
    server.close()


sendEmail(sender_email, password, to_email, message)
