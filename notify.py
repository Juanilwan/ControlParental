from dotenv import load_dotenv
from notifypy import Notify
import smtplib, random, encrypter2, os, timeH, base64
import encrypter2, imghdr
from email.message import EmailMessage

def notify():
    notification = Notify()
    notification.title = "Aviso de Control Parental"
    notification.message = "Control Parental va a apagar tu dispositivo."
    notification.icon = "logo.ico"
    notification.send()
    
def notifyNoneWifi():
        notification = Notify()
        notification.title = "Aviso de Control Parental"
        notification.message = "Control Parental no funciona correctamente debido a la falta de WIFI y va a apagar tu dispositivo."
        notification.icon = "logo.ico"
        notification.send()

def FiveMinutes():
    notification = Notify()
    notification.title = "Aviso de Control Parental"
    notification.message = "Control Parental va a apagar tu dispositivo en 5 minutos."
    notification.icon = "logo.ico"
    notification.send()
    
def mail():
    load_dotenv()
    mail = timeH.getMail()
    
    message = ("Has detenido los horarios establecidos para el dispositivo "+os.environ['COMPUTERNAME'])
    subject = "Has realizado cambios en el Control Parental"
    
    message = 'Subject: {}\n\n{}'.format(subject, message)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupiterprotectionsystem@gmail.com', encrypter2.desencriptar(os.environ['password']))
    
    server.sendmail('jupiterprotectionsystem@gmail.com', mail, message)
    
    server.quit()    
    
def webMail(x):
    load_dotenv()
    mail = timeH.getMail()
    
    if x ==0:
        message = ("Has desactivado las restricciones de paginas web en el dispositivo "+os.environ['COMPUTERNAME']+".")
        subject = "Has desactivado el bloqueo de paginas web"
    else:
        message = ("Has modificado la lista de paginas web bloqueadas para el dispositivo "+os.environ['COMPUTERNAME']+". Las paginas bloqueadas son:",x)
        subject = "Has modificado las paginas webs bloqueadas"
    
    message = 'Subject: {}\n\n{}'.format(subject, message)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupiterprotectionsystem@gmail.com', encrypter2.desencriptar(os.environ['password']))
    
    server.sendmail('jupiterprotectionsystem@gmail.com', mail, message)
    
    server.quit()   
    
def password():
    load_dotenv()
    mail = timeH.getID()[1]
    code = str(random.randint(11111, 99999))

    message = ("Tu codigo para el cambio de clave es: "+code)
    subject = ("Cambio de clave de acceso")
    
    message = 'Subject: {}\n\n{}'.format(subject, message)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupiterprotectionsystem@gmail.com', encrypter2.desencriptar(os.environ['password']))
    
    
    server.sendmail('jupiterprotectionsystem@gmail.com', mail, message)
    
    server.quit()
    print("Done")
    return code

def changeMail(x):
    load_dotenv()
    mail = timeH.getID()[1]
    code = str(random.randint(11111, 99999))

    message = ("Has solicitado cambiar tu correo electronico del control parental a: "+x+". Tu codigo para el cambio de clave es: "+code+". La solicitud de cambio de correo electronico se ha realizado desde el dispositivo: "+os.environ['COMPUTERNAME']+".")
    subject = ("Cambio de correo electronico")
    
    message = 'Subject: {}\n\n{}'.format(subject, message)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupiterprotectionsystem@gmail.com', encrypter2.desencriptar(os.environ['password']))
    
    server.sendmail('jupiterprotectionsystem@gmail.com', mail, message)
    
    server.quit()
    return code

def timeCreated():
    load_dotenv()
    mail = timeH.getMail()
    

    message = ("Has activado un horario de uso en el dispositivo "+os.environ['COMPUTERNAME']+".")
    subject = "Control de Horario Activado"
    
    message = 'Subject: {}\n\n{}'.format(subject, message)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupiterprotectionsystem@gmail.com', encrypter2.desencriptar(os.environ['password']))
    
    server.sendmail('jupiterprotectionsystem@gmail.com', mail, message)
    
    server.quit()   
    
def attack():
    load_dotenv()
    mail = timeH.getMail()
    

    message = ("El dispositivo "+os.environ['COMPUTERNAME']+" ha realizado un intento de inicio de sesion malicioso. El inicio de sesion ha sido impedido, te recomendamos que revises las funciones de seguridad activadas en el dispositivo y cambies la clave de acceso. Este ataque ha sido realizado manualmente desde el dispositivo.")
    subject = "Control Parental bajo ataque"
    
    message = 'Subject: {}\n\n{}'.format(subject, message)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupiterprotectionsystem@gmail.com', encrypter2.desencriptar(os.environ['password']))
    
    server.sendmail('jupiterprotectionsystem@gmail.com', mail, message)
    
    server.quit()  
    
def appUnlocked(x):
    load_dotenv()
    mail = timeH.getMail()
    

    message = ("Control Parental no puede bloquear la aplicacion '"+x+"' en el dispositivo "+os.environ['COMPUTERNAME']+". Esto se puede deber a que: La aplicacion ha dejado de existir o que el control parental ha sido manipulado. Te recomendamos comprobar el dispositivo para solucionar el problema. Puedes volver a bloquear la aplicacion si sigue instalada en el dispositivo.")
    subject = "Control Parental no puede bloquear una aplicacion"
    
    message = 'Subject: {}\n\n{}'.format(subject, message)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupiterprotectionsystem@gmail.com', encrypter2.desencriptar(os.environ['password']))
    
    server.sendmail('jupiterprotectionsystem@gmail.com', mail, message)
    
    server.quit()   
    
def changePassword(x, y):
    load_dotenv()
    mail = y
    

    message = ("Has olvidado la clave de tu cuenta."+ " Se ha pedido el reseteo en el dispositivo "+os.environ['COMPUTERNAME']+". La clave de tu cuenta se ha establecido en "+x+". Una vez recuperada la cuenta, puedes establecer una nueva clave.")
    subject = "Recuperar la Clave"
    
    message = 'Subject: {}\n\n{}'.format(subject, message)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupiterprotectionsystem@gmail.com', encrypter2.desencriptar(os.environ['password']))
    
    server.sendmail('jupiterprotectionsystem@gmail.com', mail, message)
    
    server.quit()
    
def codePanel(font, email, subject, code):
    load_dotenv()
    
    message = 'Subject: {}\n\n{}'.format(subject, ("El codigo en "+font+" es: "+encrypter2.desencriptar(code)))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupiterprotectionsystem@gmail.com', encrypter2.desencriptar(os.environ['password']))
    
    server.sendmail('jupiterprotectionsystem@gmail.com', email, message)
    server.quit()
    
def cameraPhoto(file, file2):
    load_dotenv()
    Sender_Email = "jupiterprotectionsystem@gmail.com"
    Reciever_Email = timeH.getID()[0]
    
    newMessage = EmailMessage()    #creating an object of EmailMessage class
    newMessage['Subject'] = "Solicitud de Imagen" #Defining email subject
    newMessage['From'] = Sender_Email  #Defining sender email
    newMessage['To'] = Reciever_Email  #Defining reciever email
    newMessage.set_content("Has solicitado imagenes del dispositivo "+os.environ['COMPUTERNAME']+".") #Defining email body
    
    with open(file, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
    with open(file2, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, encrypter2.desencriptar(os.environ['password'])) #Login to SMTP server
        smtp.send_message(newMessage)      #Sending email using send_message method by passing EmailMessage object