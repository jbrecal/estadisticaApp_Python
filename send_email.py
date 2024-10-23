from email.mime.text import MIMEText
import smtplib

def send_email(email, price, avarage_price, count): 
    from_email = "fWgk0@example.com" # put here your email
    from_password = "your_password" # put here your password
    to_email = email
    subject = "Precio de alquiler en España"
    message = "Hola, <br><br> Muchas gracias por participar en nuestro recopilador de datos.<br><br> El precio que pagas actualmente de alquiler es de <strong>%s</strong>€. La media del precio del alquiler en España está en <strong>%s</strong>€, este dato se calcula a partir de <strong>%s</strong> personas que han accedido a nuestra web. <br><br> Gracias por participar." % (price, avarage_price, count)
    
    
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
   
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    
    
    gmail.send_message(msg)
    gmail.quit()
