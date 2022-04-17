import mysql.connector, timeH, time, hashlib, notify, ctypes, notify, encrypter2, random
import tkinter as tk

def startConnection():
    global mycursor, mydb
    print("Login")
    try:
        mydb = mysql.connector.connect(
          host="sql11.freesqldatabase.com",
          user="sql11484859",
          password="VSXRIJdzjX",
          database = "sql11484859"
        )
        mydb.autocommit = True
        mycursor = mydb.cursor()
    except: 
        time.sleep(2)
        print(1)
        startConnection()

def login(Coel, password):
    print("2")
    sql = "SELECT CO FROM MDMdata"
    print(2.0)
    startConnection()
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    print(2.1)
    uslist = []
    
    for i in myresult: uslist.append(i[0])
    
    for name in uslist:
        if name == Coel:
            print(name)
            print(Coel)
            sql = "SELECT Password FROM MDMdata WHERE CO = %s"
            adr = (Coel, )
            
            mycursor.execute(sql, adr)
            
            myresult = mycursor.fetchall()
            myresult = myresult[0]
            print(2.5)
            if timeH.encrypt(password, 0, None) == myresult[0]: return True
            else: return False
    print(2.5)
    return False
        
def getActualTime(mode):
    try:
        sql = "SELECT actualTime FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        return myresult[0]
    except:
        time.sleep(2)
        print(2)
        startConnection()
        return getActualTime(mode)
        
def getMaxTime(mode):
    try:
        sql = "SELECT maxTime FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        
        return (myresult[0])
    except:
        time.sleep(2)
        print(3)
        startConnection()
        return getMaxTime(mode)
        
def getResetTime(mode):
    try: 
        sql = "SELECT resetTime FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        return (myresult[0])
    except: 
        time.sleep(2)
        print(4)
        startConnection()
        return getResetTime(mode)
        
def setTimer(x, y, z, mode):
    try:
        # startConnection()
        sql = "UPDATE MDMdata SET actualTime = %s, maxTime = %s, resetTime = %s WHERE CO = %s"
        adr = (x, y, z, timeH.getID()[mode],)
        
        mycursor.execute(sql, adr)
        mydb.commit()
    except:
        time.sleep(2)
        print(5)
        startConnection()
        setTimer(x, y, z, mode)
        
    
def getTime(mode):  
    try:
        # startConnection()
        sql = "SELECT shutdownTime FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        return (myresult[0])
    except: 
        time.sleep(2)
        print(6)
        startConnection()
        return getTime(mode)
        
def getOpenTime(mode):
    try:
        # startConnection()
        sql = "SELECT openShutdownTime FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        return (myresult[0])
    except: 
        time.sleep(2)
        print(7)
        startConnection()
        return getOpenTime(mode)

def IRepeat(mode):
    try:
        # startConnection()
        sql = "SELECT Irepeat FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        mycursor.execute(sql, adr)
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        return (myresult[0])
    except: 
        time.sleep(2)
        print(8)
        startConnection()
        return IRepeat(mode)
        
def changeTime(x, y, z, mode):
    try:
        # startConnection()
        sql = "UPDATE MDMdata SET shutdownTime = %s, openShutdownTime = %s, Irepeat = %s WHERE CO = %s"
        adr = (x, y, z, timeH.getID()[mode],)
        mycursor.execute(sql, adr)
        mydb.commit()
    except: 
        time.sleep(2)
        print(9)
        startConnection()
        changeTime(x, y, z, mode)
        
def getWebs(mode):
    try:
        sql = "SELECT blockedWebsites FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]

        return myresult[0]
    except: 
        time.sleep(2)
        print(10)
        startConnection()
        return getWebs(mode)
        
def setWebs(x, mode):
    try:
        startConnection()
        sql = "UPDATE MDMdata SET blockedWebsites = %s WHERE CO = %s"
        adr = (x, timeH.getID()[mode],)
        mycursor.execute(sql, adr)
        mydb.commit()
    except: 
        time.sleep(2)
        print(11)
        startConnection()
        setWebs(x, mode)
        
def password(x, mode):
    #Mode O only return the code encrypted, Mode 1 change the code, Mode 2 return the account code
    try:
        startConnection()
        if mode == 0: 
            m = hashlib.md5(bytes(x.encode(encoding='UTF-8'))).hexdigest()
            return m
        
        elif mode == 1: 
            m = hashlib.md5(bytes(x.encode(encoding='UTF-8'))).hexdigest()
            
            sql = "UPDATE MDMdata SET Password = %s WHERE CO = %s"
            adr = (m, timeH.getID()[1],)
            mycursor.execute(sql, adr)
            mydb.commit()
            print(x)
            print("Changed")
    
        else: 
           sql = "SELECT Password FROM MDMdata WHERE CO = %s"
           adr = (timeH.getID()[1], )
        
           mycursor.execute(sql, adr)
        
           myresult = mycursor.fetchall()
           myresult = myresult[0]
           return (myresult[0]) 
            
    except:
        time.sleep(2)
        print(12)
        startConnection()
        password(x, mode)
        
def changeMail(CO, Id):
    try:
        sql = "UPDATE MDMdata SET CO = %s WHERE CO = %s"
        adr = (CO, Id,)
        mycursor.execute(sql, adr)
        mydb.commit()
        if timeH.getID()[1] == timeH.getID()[0]: timeH.setID(CO, CO)
        else: timeH.setID(timeH.getID()[0], CO)
            
    except:
        print(13)
        startConnection()
        changeMail(CO, Id)  
        
def getCamera(mode):
    try:
        sql = "SELECT camera FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]

        return myresult[0]
    except: 
        time.sleep(1.33)
        print(14)
        startConnection()
        return getCamera(mode)
    
def getStore(mode):
    try:
        sql = "SELECT MicrosoftStore FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
    
        return myresult[0]
    except: 
        time.sleep(1.33)
        print(14)
        startConnection()
        return getStore(mode)
    
def getSkype(mode):
    try:
        sql = "SELECT Skype FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
    
        return myresult[0]
    except: 
        time.sleep(1.33)
        print(15)
        startConnection()
        return getSkype(mode)
    
def getBrowser(mode):
    try:
        sql = "SELECT Browser FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
    
        return myresult[0]
    except: 
        time.sleep(1.33)
        print(15)
        startConnection()
        return getBrowser(mode)
    

def setRestrictions(cam, stor, sky, brow, mode):
    try:
        # startConnection()
        sql = "UPDATE MDMdata SET Camera = %s, MicrosoftStore = %s, Skype = %s, Browser = %s WHERE CO = %s"
        adr = (cam, stor, sky, brow, timeH.getID()[mode],)
        mycursor.execute(sql, adr)
        mydb.commit()
    except: 
        time.sleep(2)
        print(16)
        startConnection()
        setRestrictions(cam, stor, sky, mode)
        
def getUser(mode):
    try:
        # startConnection()
        sql = "SELECT Username FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        return (myresult[0])
    except: 
        time.sleep(2)
        print(17)
        startConnection()
        return getUser(mode)
        
def recoverPassword(cor):
    try:
        # startConnection()
        sql = "SELECT CO FROM MDMdata"
        var = mycursor.execute(sql)
        var = mycursor.fetchall()
        uslist = []
    
        for i in var: uslist.append(i[0])
        print(var, uslist)
        if cor in uslist:
            pas = timeH.genPassword()
            sql = "UPDATE MDMdata SET Password = %s WHERE CO = %s"
            adr = (timeH.encrypt(pas, 0, None), cor,)
            mycursor.execute(sql, adr)
            mydb.commit()
            notify.changePassword(pas, cor)
            ctypes.windll.user32.MessageBoxW(0, "Tu contraseña ha sido cambiada. Se ha enviado tu nueva contraseña a tu correo electrónico.",  "Contraseña Cambiada")
        else: ctypes.windll.user32.MessageBoxW(0, "El correo electrónico introducido no está registrado.",  "¡Aviso Importante!")
    except: 
        time.sleep(2)
        startConnection()
        recoverPassword(cor)
    
def checkCO(cor):
    try:
        startConnection()
        sql = "SELECT CO FROM MDMdata"
        var = mycursor.execute(sql)
        var = mycursor.fetchall()
        uslist = []
        for i in var: uslist.append(i[0])
        
        if cor in uslist: return True
        else: return False
    except:
        time.sleep(2)
        print(18)
        startConnection()
        checkCO(cor)
        
        
        
def createAccount(us, cor, pas):
    try:
        pas = timeH.encrypt(pas, 0, None)
        startConnection()
        mycursor = mydb.cursor()
        sql = "INSERT INTO MDMdata (Username, CO, Password) VALUES (%s, %s, %s)"
        val = (us, cor, pas)
        mycursor.execute(sql, val)
        mydb.commit()
        
    except:
        print("ERROR")
        print(19)
        startConnection()
        createAccount(us, cor, pas)
        

def codeCheck(title, font, email, subject):
    def interface():
        result = None
        def entryCheck(x, y):
            global result
            panel.destroy()
            panel.quit()
            if x==y: result = True
            else: result = False
              
        code=str(encrypter2.encriptar(random.randint(1500, 9999)-random.randint(0, 500)))
        notify.codePanel(font, email, subject, code)
        panel = tk.Toplevel()
        panel.geometry("300x150")
        panel.title(title)
        panel.resizable(False, False)
        tk.Label(panel, font="Montserrat 2").pack()
        tk.Label(panel, text=title, font="Montserrat 12 bold").pack()
        tk.Label(panel, text=email, font="Montserrat 9").pack()
        tk.Label(panel, text="Introduce el Código:").place(x=10, y=63)    
        box = tk.Entry(panel, show="*", width=6)
        box.place(x=135, y=66)
        loadimage1 = tk.PhotoImage(file="checkButton.png")
        checkButton = tk.Button(panel, image=loadimage1, border=0, command=lambda: entryCheck(box.get(), encrypter2.desencriptar(code)[:-1]))
        checkButton.place(x=85, y=95)
        panel.mainloop()
    interface()
    return result   

#0 applies the queue, 1 establish None, 2 establish (process is used here, only for temporal user)
def queue(sel, process):
    if sel == 0:
      try:
        sql = "SELECT Queue FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[0], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        return (myresult[0])
      except: 
         startConnection()
         return queue(0, None)
    elif sel == 1:
        try:
            sql = "UPDATE MDMdata SET Queue = %s WHERE CO = %s"
            adr = ("None", timeH.getID()[0],)
            mycursor.execute(sql, adr)
            mydb.commit()
        except:
            startConnection()
            queue(1, None)
    else:
        try:
            sql = "UPDATE MDMdata SET Queue = %s WHERE CO = %s"
            adr = (process, timeH.getID()[1],)
            mycursor.execute(sql, adr)
            mydb.commit()
        except:
            startConnection()
            queue(2, process)
            
# 0 to obtain the image, 1 to upload it
def picture(sel, mode, image):
    if sel == 0:
      try:
        sql = "SELECT Picture FROM MDMdata WHERE CO = %s"
        adr = (timeH.getID()[mode], )
        
        mycursor.execute(sql, adr)
        
        myresult = mycursor.fetchall()
        myresult = myresult[0]
        return (myresult[0])
    
      except: 
         startConnection()
         return picture(sel, mode, image)
     
    elif sel == 1:
        try:
            sql = "UPDATE MDMdata SET Picture = %s WHERE CO = %s"
            adr = (image, timeH.getID()[mode],)
            mycursor.execute(sql, adr)
            mydb.commit()
        except:
            startConnection()
            picture(sel, mode, image)