import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import calendar, time, timeH, websiteBlocker, datetime, keyboard, historial, database

logged = False
userID = None
horario = 7200 #3600-> Horario de Invierno, 7200-> Horario de Verano

def dashboard():
    global logged
    logged = True
    picture = database.picture(0, 1, None)
    if picture == "Unknown": picture = loadimage6
    elif picture == "Mike": picture = loadimage8
    elif picture == "Minion": picture = loadimage9
    
    def stopRun(): 
        database.changeTime(0, 86400, 0, 1)
    
    def settingPage():
        def close():
            root.destroy()
            rootSet.destroy()
            load()
        def changeData(data):
            if data == "password": dataElement = "Contraseña"
            else: dataElement = "Correo Electrónico"
            def checkChange(x, y, z, mode):                                        
                if mode == 0:
                    if database.password(x, 0) == database.password(None, 2) and y == z and x!=y and x!=z: 
                      if z!="" and z!=" " and z!="  " and z!="   " and z!="     "and z!="      ":
                        if database.codeCheck("Cambiar Contraseña", "Jupiter Protection", timeH.getID()[1], "Cambiar Clave"): 
                            database.password(z, 1)
                            ps.destroy()
                        else: messagebox.showinfo(message="La clave introducida no es correcta.", title="Clave Incorrecta")
                      else: messagebox.showinfo(message="La contraseña elegida es muy poco segura.", title="Aviso Importante")
                    else: messagebox.showinfo(message="Las contraseñas nuevas no coinciden o la contraseña antigua introducida es incorrecta. El error se puede deber a que has usado la misma contraseña.", title="Aviso Importante")
                else:
                   if x == timeH.getID()[1] and y == z and timeH.getID()[1]!=y and timeH.getID()[1]!=z: 
                       if database.checkCO(z) == False:
                        if database.codeCheck("Cambiar Correo Electrónico", "Jupiter Protection", timeH.getID()[1], "Cambiar Correo Electronico") == True:
                            database.changeMail(y, timeH.getID()[1])  
                            ps.destroy()
                        else: messagebox.showinfo(message="La clave introducida no es correcta.", title="Clave Incorrecta")
                       else: messagebox.showinfo(message="El correo introducido ya está registrado.", title="Aviso Importante")
                   else: messagebox.showinfo(message="Uno o más de los datos introducidos es incorrecto. A lo mejor has usado el mismo correo electrónico.", title="Aviso Importante")
            
            rootSet.destroy()
            
            ps = tk.Tk()
            ps.resizable(False, False)
            ps.title("Cambiar " + dataElement)
            ps.iconbitmap("logo.ico")
            if data != "password": ps.geometry("450x200") 
            else: ps.geometry("300x200") 
            
            if dataElement == "Contraseña": 
                ap = tk.Entry(ps, show="*", width=15)
                tk.Label(ps, text="Antigua "+ dataElement+":").place(x=10, y=10)
            else:  
                tk.Label(ps, text="Antiguo "+ dataElement+":").place(x=10, y=10)
                ap = tk.Entry(ps, width=30)
            ap.place(x=180, y=13)
            
            if dataElement == "Contraseña": 
                np = tk.Entry(ps, width=15, show="*")
                tk.Label(ps, text="Nueva "+ dataElement+":").place(x=10, y=50)
            else:   
                tk.Label(ps, text="Nuevo "+ dataElement+":").place(x=10, y=50)
                np = tk.Entry(ps, width=30)
            np.place(x=180, y=53)
            
            tk.Label(ps, text="Repetir "+ dataElement+":").place(x=10, y=90)
            if dataElement == "Contraseña": rp = tk.Entry(ps, width=15, show="*")
            else: rp = tk.Entry(ps, width=30)
            rp.place(x=180, y=93)
            
            cp = tk.Button(ps, text=("Cambiar "+ dataElement))
            if dataElement == "Contraseña": cp.config(command = lambda: checkChange(ap.get(), np.get(), rp.get(), 0))
            else: cp.config(command = lambda: checkChange(ap.get(), np.get(), rp.get(), 1))
            cp.place(x=120, y=143)
        
        
        def pairing():
            global pairedText
            mail = timeH.getID()[0]
            x = timeH.getID()[1]
            
            if mail == "Unconnected":
                timeH.setID(x, x)
                pairedText = "Desvincular Dispositivo"
                rootSet.destroy()
            elif mail == x:
                timeH.setID("Unconnected", x)
                websiteBlocker.unblock(0)
                pairedText = "Vincular Dispositivo"
                rootSet.destroy()
            else: pass
        
        def recharge():
            global userID
            root.destroy()
            rootSet.destroy()
            load()
            timeH.setID(timeH.getID()[0], userID)
            dashboard()
            root.geometry("690x350")
        
        rootSet = tk.Tk()
        rootSet.resizable(False, False)
        rootSet.iconbitmap("logo.ico")
        rootSet.title("Ajustes")
        rootSet.geometry("300x200")
        
        contraseñaB = tk.Button(rootSet, text="Cambiar Contraseña", command= lambda: changeData("password")).pack()
        
        correoB = tk.Button(rootSet, text="Cambiar Correo Electrónico", command= lambda: changeData("correo")).pack()
        
        
        pairedText =  ""
        if timeH.getID()[0] == timeH.getID()[1]: pairedText = "Desvincular Dispositivo" 
        elif timeH.getID()[0] == "Unconnected": pairedText = "Vincular Dispositivo" 
        else: pairedText = "Vinculación Desactivada"
            
        pairingB = tk.Button(rootSet, text=pairedText, command=lambda: pairing()).pack()
        
        rechargeB = tk.Button(rootSet, text="Recargar Cuenta", command= lambda: recharge()).pack()
        
        cerrarB = tk.Button(rootSet, text="Cerrar Sesión", command = lambda: close()).pack()
    
    def update(x,y,rep):
        if x == " " or x == "" or x == "0" or x == "0:00" or x=="00:00" or x=="" or x=="0:0":
            if y == " " or y == "" or y == "0" or y == "0:00" or y=="00:00" or y==""or y=="0:0":
                stopRun()
                timetable.set("No hay horarios establecidos")
                return
        #Hora de Cierre
        z = x.split(":")

        d = time.strftime("%d", time.localtime(time.time()))
        m = time.strftime("%m", time.localtime(time.time()))
        finalHour = (calendar.timegm(time.strptime(f'2022-{m}-{d} {z[0]}:{z[1]}:00', '%Y-%m-%d %H:%M:%S')))-horario
        
        #Hora de Apertura
        
        a = y.split(":")

        oHour = (calendar.timegm(time.strptime(f'2022-{m}-{d} {a[0]}:{a[1]}:00', '%Y-%m-%d %H:%M:%S')))-horario
        
        if oHour < finalHour: oHour = int(oHour)+86400
        if finalHour < time.time() and oHour < time.time():
            
            finalHour += 86400
            oHour += 86400
        
        database.changeTime(finalHour, oHour, rep, 1)

        timetable.set("Restricción de horario: "+ time.strftime("%H:%M", time.localtime(database.getTime(1)))+" - "+ time.strftime("%H:%M", time.localtime(database.getOpenTime(1))))
    
    cameraButton = tk.Button(root, image=loadimage7, border = 0, command=lambda: database.queue(2, "Camera"))
    cameraButton.place(x=10, y=10)
    
    coEntry.destroy()
    passEntry.destroy()
    accessButton.destroy()
    coText.destroy()
    paText.destroy()
    recoverButton.destroy()
    createButton.destroy()
    
    # Foto de Perfil
    tk.Label(root, image=picture).pack()
    
    settingButton = tk.Button(root, image=loadimage2, border = 0, command=settingPage)
    settingButton.place(x=650, y=0)
    
    timeText = tk.StringVar()
    if database.getMaxTime(1) <90000: timeText.set("Restricción de tiempo: "+ str(datetime.timedelta(seconds= database.getMaxTime(1))))
    else: timeText.set("No hay restricciones de tiempo")
    
    
    #Control de Tiempo
    
    def pubMaxTime(x, kind, mode):
        if x == "0" or x == "0:00" or x=="00:00" or x==""or x=="0:0" or x==" ":
            pubMaxTime(None, 1, None)
            return
            
        if kind == 0:
            if mode == "Minutos":
                if int(x) > 1440 or int(x)<=0: pass
                elif int(x) == 1440: 
                    database.setTimer(database.getActualTime(1), 86399, database.getResetTime(1), 1)
                    timeText.set("Restricción de tiempo: "+ str(datetime.timedelta(seconds= database.getMaxTime(1))))
                else:
                    x = int(x)*60
                    database.setTimer(database.getActualTime(1), x, database.getResetTime(1), 1)
                    timeText.set("Restricción de tiempo: "+ str(datetime.timedelta(seconds= database.getMaxTime(1))))
            elif mode == "Horas":
                if int(x) >= 25 or int(x)<=0: pass
                elif int(x) == 24:  
                    database.setTimer(database.getActualTime(1), 86399, database.getResetTime(1), 1)
                    timeText.set("Restricción de tiempo: "+ str(datetime.timedelta(seconds= database.getMaxTime(1))))
                else:
                    x = int(x)*3600
                    database.setTimer(database.getActualTime(1), x, database.getResetTime(1), 1)
                    timeText.set("Restricción de tiempo: "+ str(datetime.timedelta(seconds= database.getMaxTime(1))))
            else: 
                UseTime = x
                y = list(UseTime)
                num = 0
                for i in y:
                    if i == ":": num +=1
                if num == 1:
                    z = UseTime.split(":")
                
                    hour = int(z[0])
                    minute = int(z[1])
                    
                    while minute >= 60 and hour <23:
                        minute = minute-60
                        hour +=1
                  
                    if hour >=0 and hour <24:
                        if minute >=0 and minute <60: 
                            result = ((hour*60*60)+(minute*60))
                            database.setTimer(database.getActualTime(1), result, database.getResetTime(1), 1)
                            timeText.set("Restricción de tiempo: "+ str(datetime.timedelta(seconds= database.getMaxTime(1))))
                    if hour == 24 and minute == 0:
                        timeH.setTimer(database.getActualTime(1), 86399, database.getResetTime(1), 1)
                        timeText.set("Restricción de tiempo: "+ str(datetime.timedelta(seconds= database.getMaxTime(1))))


                
        else: 
            database.setTimer(database.getActualTime(1), 90000, database.getResetTime(1), 1)
            timeText.set("No hay restricciones de tiempo")
            
    def restrictions():
        global hourText, openHourText
        def applyChanges(cam, stor, sky, brow, web):
            if cam == "Permitida": cam = "True"
            else: cam = "False"
            
            if stor == "Permitida": stor = "True"
            else: stor = "False"
            
            if sky == "Permitida": sky = "True"
            else: sky = "False"
            
            if brow == "Permitidos": brow = "True"
            else: brow = "False"
            
            database.setRestrictions(cam, stor, sky, brow, 1)
            pubMaxTime(timeSet.get(), 0, modeSelector.get())
            
            if repiteSelector.get() == "Repetir Diariamente": rep = 1
            else: rep = 0

            update(hour.get(), openHour.get(), rep)      
            
            if web == "Bloquear": websiteBlocker.block(pageEntry.get(), 1)
            else: websiteBlocker.unblockS(pageEntry.get(), 1)
            

        res = tk.Toplevel()
        res.title("Restricciones")
        res.geometry("550x425")
        res.resizable(False, False)
        res.iconbitmap("logo.ico")
        
        
        historialButton = tk.Button(res, image=loadimage3, border = 0, command=lambda: historial.generate())
        historialButton.place(x=295, y=0)
        
        restrictedButton = tk.Button(res, image=loadimage5, border = 0, command=lambda: websiteBlocker.restrictedPages())
        restrictedButton.place(x=295, y=40)
        
        
        tk.Label(res, text="Cámara:").place(x=10, y=10)
        camSelector = ttk.Combobox(res, state="readonly", width=15)
        camSelector["values"] = ["Permitida", "Bloqueada"]
        if database.getCamera(1) == "True": camSelector.set("Permitida")
        else: camSelector.set("Bloqueada")
        camSelector.place(x=80, y=10)
        tk.Label(res, text="Microsoft Store:").place(x=10, y=50)
        storeSelector = ttk.Combobox(res, state="readonly", width=15)
        storeSelector["values"] = ["Permitida", "Bloqueada"]
        if database.getStore(1) == "True": storeSelector.set("Permitida")
        else: storeSelector.set("Bloqueada")
        storeSelector.place(x=110, y=50)
        tk.Label(res, text="Skype:").place(x=10, y=90)
        skySelector = ttk.Combobox(res, state="readonly", width=15)
        skySelector["values"] = ["Permitida", "Bloqueada"]
        if database.getSkype(1) == "True": skySelector.set("Permitida")
        else: skySelector.set("Bloqueada")
        skySelector.place(x=60, y=90)
        
        tk.Label(res, text="Navegadores de Internet:").place(x=10, y=130)
        browSelector = ttk.Combobox(res, state="readonly", width=15)
        browSelector["values"] = ["Permitidos", "Bloqueados"]
        if database.getBrowser(1) == "True": browSelector.set("Permitidos")
        else: browSelector.set("Bloqueados")
        browSelector.place(x=160, y=130)
        
        mTime = database.getMaxTime(1)
        if mTime == 90000:
            mTime=""
        else: 
            mTime = str(datetime.timedelta(seconds=int(mTime)))
            mTime = mTime.split(":")
            mTime = str(mTime[0]+":"+mTime[1])
            
        ct1 = tk.StringVar(value=mTime)
        ct1=ct1.get()
        
        tk.Label(res, text="Establecer limite de tiempo:").place(x=10, y = 170)
        timeSet = tk.Entry(res, width=8)
        timeSet.insert(0, ct1)
        timeSet.place(x=180, y= 173)
        
        modeSelector = ttk.Combobox(res, state="readonly", width=15)
        modeSelector["values"] = ["Horas", "Minutos", "Horas:Minutos"]
        modeSelector.set("Horas:Minutos")
        modeSelector.place(x=240, y=170)   
        
        tk.Label(res, text="Hora de Bloqueo:").place(x=10, y=210)
        hourText = tk.StringVar()
        if database.getTime(1) != 0: hourText.set(time.strftime("%H:%M", time.localtime(database.getTime(1))))    
        hour = tk.Entry(res, width=10)
        hour.insert(0, hourText.get())
        hour.place(x=130, y=213)
        tk.Label(res, text="Hora de Desbloqueo:").place(x=10, y=250)
        openHourText = tk.StringVar()
        if database.getTime(1) != 0:openHourText.set(time.strftime("%H:%M", time.localtime(database.getOpenTime(1))))   
        openHour = tk.Entry(res, width=10)
        openHour.insert(0, openHourText.get())
        openHour.place(x=130, y=253)
        
        repiteSelector = ttk.Combobox(res, state="readonly", width=23)
        repiteSelector["values"] = ["Repetir Diariamente", "No Repetir Diariamente"]
        if database.IRepeat(1)== 0: repiteSelector.set("No Repetir Diariamente")
        else: repiteSelector.set("Repetir Diariamente")
        repiteSelector.place(x=210, y=233)  
        
        
        #Area de Paginas Web
    
        tk.Label(res, text="Página Web:").place(x=10, y=290)
        pageEntry = tk.Entry(res, width=20)
        pageEntry.place(x=100, y=293)
        
        webModeSelector = ttk.Combobox(res, state="readonly", width=15)
        webModeSelector["values"] = ["Bloquear", "Desbloquear"]
        webModeSelector.set("Bloquear")
        webModeSelector.place(x=240, y=293)   
        
        unblockEButton = tk.Button(res, text="Desbloquear Todo", command= lambda: websiteBlocker.unblock(1))
        unblockEButton.place(x=380, y=293)
        
        blockGoogle = tk.Button(res, text="Bloquear Google", command= lambda: websiteBlocker.Google(1))
        blockGoogle.place(x=10, y=326)
        
        unblockGoogle = tk.Button(res, text="Desbloquear Google", command= lambda: websiteBlocker.Google(0))
        unblockGoogle.place(x=140, y=326)
        
        pubButton = tk.Button(res, image=loadimage4, border = 0, command = lambda: applyChanges(camSelector.get(), storeSelector.get(), skySelector.get(), browSelector.get(), webModeSelector.get()))
        pubButton.place(x=220, y=370)
           
    usedTime = str(datetime.timedelta(seconds= database.getActualTime(1)))
    
    restrictionButton = tk.Button(root, image=loadimage1, border = 0, command = restrictions)
    restrictionButton.place(x=615, y=280)
    
    tk.Label(root, text=time.strftime("%H:%M", time.localtime(time.time())), font="Helvetica 14 bold").pack()
    pres = tk.Label(root, text=("Bienvenido/a "+database.getUser(1)), font='Helvetica 14 bold').pack()
    
    database.getActualTime(1)
    textTime = str(datetime.timedelta(seconds= database.getActualTime(1)))
    textTime = textTime.split(":")
    textTime = (textTime[0]+"h "+textTime[1]+"m "+textTime[2]+"s")
    tk.Label(root, font='Helvetica 14 bold', text = textTime).pack()
    maxTimeLabel = tk.Label(root, textvariable = timeText, font='Helvetica 13 bold').pack()
    
    timetable = tk.StringVar()
    if database.getTime(1) == 0: 
        timetable.set("No hay horarios establecidos")
    else: 
        timetable.set("Restricción de horario: "+ time.strftime("%H:%M", time.localtime(database.getTime(1)))+" - "+ time.strftime("%H:%M", time.localtime(database.getOpenTime(1))))

    timetableLabel = tk.Label(root, textvariable=timetable, font='Helvetica 13 bold')
    timetableLabel.pack()
    
def check(x, y):
    global userID
    if database.login(x, y): 
        
        if timeH.getID()[0] == "": timeH.setID(x, x)  
        elif x != timeH.getID()[0] and timeH.getID()[0]!= "":
            timeH.setID(timeH.getID()[0], x)
            if timeH.getID()[0] != "Unconnected": messagebox.showinfo(message="Este dispositivo está vinculado a otra cuenta de Jupiter Protection. Los cambios que realizes se publicarán en los dispositivos vinculados a tu cuenta.", title="Aviso Importante")
        else: timeH.setID(x, x)
        root.geometry("690x350")
        userID = timeH.getID()[1]
        dashboard()
    else: 
        messagebox.showinfo(message="Usuario o contraseña incorrectos.", title="Error de Inicio de Sesión")
    
def recover():
    cf = tk.Tk()
    cf.resizable(False, False)
    cf.title("Recuperar Contraseña")
    cf.geometry("400x135")
    
    tk.Label(cf, text="Correo Electrónico:").place(x=10, y=10)
    box = tk.Entry(cf, width=25)
    box.place(x=135, y=13)
    
    FButton = tk.Button(cf, text="Recuperar Contraseña", command= lambda: database.recoverPassword(box.get()))
    FButton.place(x=80, y =70)

def createAccount():
    def create(nom, cor, con, rcon):
        if con == rcon: 
            if nom != "" and cor != "" and con !="":
                if database.checkCO(cor): messagebox.showinfo(message="El correo electrónico introducido ya está registrado.", title="Error al Crear Cuenta")
                else: 
                    cf.destroy()
                    if database.codeCheck("Crear Cuenta", "Jupiter Protection", cor, "Crear Cuenta en Jupiter Protection"): 
                        database.createAccount(nom, cor, con)
                        check(cor, con)
                    else: messagebox.showinfo(message="El código introducido no es válido. Intentelo de nuevo.", title="Error al Crear Cuenta")
                    
            else: messagebox.showinfo(message="Los espacios no pueden estar en blanco.", title="Error al Crear Cuenta")
        else: messagebox.showinfo(message="Las contraseñas no coinciden.", title="Error al Crear Cuenta")
    
    cf = tk.Tk()
    cf.resizable(False, False)
    cf.title("Crear Cuenta")
    cf.geometry("400x300")
    
    tk.Label(cf, text="Nombre de Usuario:").place(x=10, y=10)
    nu = tk.Entry(cf, width=20)
    nu.place(x=135, y=13)
    
    tk.Label(cf, text= "Correo Electrónico:").place(x=10, y=60)
    co = tk.Entry(cf, width=25)
    co.place(x=135, y =63)

    tk.Label(cf, text="Contraseña:").place(x=10, y=110)
    pas = tk.Entry(cf, width=25, show="*")
    pas.place(x=135, y=113)
    
    tk.Label(cf, text="Repetir Contraseña:").place(x=10, y=160)
    rpas = tk.Entry(cf, width=25, show="*")
    rpas.place(x=135, y=163)
    
    createB = tk.Button(cf, text="Crear Cuenta", command= lambda: create(nu.get(), co.get(), pas.get(), rpas.get()))
    createB.place(x=135, y=210)

def load():
    global root, coEntry, passEntry, accessButton, coText, paText, createButton, recoverButton, loadimage1, loadimage2, loadimage3, loadimage4, loadimage5, loadimage6, loadimage7, loadimage8, loadimage9
    root = tk.Tk()
    root.geometry("690x300")
    root.resizable(False, False)
    root.title("Security Management System")
    root.iconbitmap("logo.ico")
    
    coText = tk.Label(root, text="Correo Electrónico:")
    coText.place(x=208, y=57)
    coEntry = tk.Entry(root, width=25)
    if timeH.getID()[0] != "Unconnected": coEntry.insert(0, timeH.getID()[0])
    coEntry.place(x=325, y =60)
    
    paText = tk.Label(root, text="Contraseña:")
    paText.place(x=249, y=107)
    passEntry = tk.Entry(root, width=25, show="*")
    passEntry.place(x=325, y =110)
    
    accessButton = tk.Button(root, text="Acceder", command = lambda: check(coEntry.get(), passEntry.get()))
    accessButton.place(x=285, y=150)
    keyboard.on_press_key("enter", lambda _: check(coEntry.get(), passEntry.get()))
    recoverButton = tk.Button(root, text="Recuperar Contraseña", command = lambda: recover())
    recoverButton.place(x=252, y=185)
    
    createButton = tk.Button(root, text="Crear Cuenta", command = lambda: createAccount())
    createButton.place(x =275, y =220)
    
    loadimage1 = tk.PhotoImage(file="restrictButton.png")
    loadimage2 = tk.PhotoImage(file="settingButton.png")
    loadimage3 = tk.PhotoImage(file="historialButton.png")
    loadimage4 = tk.PhotoImage(file="publishButton.png")
    loadimage5 = tk.PhotoImage(file="restrictedButton.png")
    loadimage6 = tk.PhotoImage(file="perfilPre.png")
    loadimage7= tk.PhotoImage(file="cameraButton.png")
    loadimage8= tk.PhotoImage(file="mikeProfile.png")
    loadimage9= tk.PhotoImage(file="minionProfile.png")
load()
root.mainloop()