import database, time, os, wmi, psutil, timeH, pygame, pygame.camera, notify, wx, subprocess


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# localhost's IP
redirect = "127.0.0.1"   

# with open(hosts_path, 'r+') as file:                    
checkerWebs = database.getWebs(0)

CamName = "WindowsCamera.exe"
StorName = "WinStore.App.exe"


f = wmi.WMI()
num = 5


def camera():
    pygame.camera.init()
      
    # make the list of all available cameras
    camlist = pygame.camera.list_cameras()
      
    # if camera is detected or not
    if camlist:
      
        # initializing the cam variable with default camera
        cam = pygame.camera.Camera(camlist[0], (640, 480))
      
        # opening the camera
        cam.start()
        os.system(f'taskkill /f /im WindowsCamera.exe')
        time.sleep(1.5)
        # capturing the single image
        image = cam.get_image()
        time.sleep(0)
        # saving the image
        nom = str(int(time.time()))+".png"
        pygame.image.save(image, nom)
        cam.stop()
        return nom
        
    # if camera is not detected the moving to else part
    else:
        print("Camera Error")
        
        
def screenshot():
    app = wx.App()  # Need to create an App instance before doing anything
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.Bitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem  # Release bitmap
    nom = str(int(time.time()))+".png"
    bmp.SaveFile(nom, wx.BITMAP_TYPE_PNG)
    return nom
    
def browserKill():
    browsers = ["chrome.exe", "firefox.exe", "msedge.exe", "opera.exe", "iexplore.exe"]
    for i in browsers: 
        if checkIfProcessRunning(i):
            os.system(f'taskkill /f /im {browsers[0]}')
            os.system(f'taskkill /f /im {browsers[1]}')
            os.system(f'taskkill /f /im {browsers[2]}')
            os.system(f'taskkill /f /im {browsers[3]}')
            os.system(f'taskkill /f /im {browsers[4]}')
            return
    

while True:
    if timeH.getID()[0] != "Unconnected":
        print("CONN")
        if num == 5:
            if timeH.getID()[0] != "Unconnected":
                cam = database.getCamera(0)
                stor = database.getStore(0)
                sky = database.getSkype(0)
                brow = database.getBrowser(0)
                process = database.queue(0, None)
                print(brow)
                browsers = ["chrome.exe", "msedge.exe", "opera.exe", "iexplore.exe", "firefox.exe"]
        if num >= 5: num = 0
        print(2)
        webs = database.getWebs(0)
        if webs == checkerWebs: pass
        else: 
          webs = webs.split(',')
          if '' in webs: webs.remove('')
          with open(hosts_path, 'r+') as file:                    
                file.truncate()
                for i in webs:
                    file.write(redirect + " " + i + "\n")
                    file.write(redirect + " " +"www."+i + "\n")
          checkerWebs = database.getWebs(0)
          print("Updated")
          print(3)
        if cam == "False": 
            if checkIfProcessRunning("WindowsCamera.exe"):  os.system(f'taskkill /f /im WindowsCamera.exe')
        if stor == "False": 
            if checkIfProcessRunning("WinStore.App.exe"):  os.system(f'taskkill /f /im WinStore.App.exe')
        if sky == "False": 
            if checkIfProcessRunning("Skype.exe"):  os.system(f'taskkill /f /im Skype.exe')
        if brow == "False": browserKill()
        
        if process == "Camera":
            notify.cameraPhoto(camera(), screenshot())
            process=None
            database.queue(1, None)
        if process == "Shutdown": 
            process=None
            database.queue(1, None)
            notify.notify()
            time.sleep(10)
            subprocess.run("shutdown -l")
            
        num +=1
    else: 
        print("DISS")
        with open(hosts_path, 'r+') as file: file.truncate()
    time.sleep(0.5)