import smtplib


def send_email(link): 
    """This function send an email"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('ma.sanchez.lr@gmail.com', '---')
    subject = "El libro ya salio!"
    body = "El link es: tushoppi.com.mx{}".format(link)
    msg = "Subject: {} \n\n {}".format(subject, body)
    server.sendmail(
        'ma.sanchez.lr@gmail.com',
        'mariesadaizp@gmail.com',
        msg
    )
    server.sendmail(
        'ma.sanchez.lr@gmail.com',
        'ma.sanchez.lr@gmail.com',
        msg
    )
    print("El correo se ha enviado")
    server.quit()

    
