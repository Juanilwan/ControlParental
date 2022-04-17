import time, subprocess, notify, database, timeH

while True: 
    try:
        if timeH.getID()[0] != "Unconnected":
            database.getTime(0)
            shutdownTime = database.getTime(0)
            openShutdownTime = database.getOpenTime(0)
            repetition = database.IRepeat(0)
            #Time Detector
            if int(time.time()) >= shutdownTime and int(time.time())<openShutdownTime:
                notify.notify()
                time.sleep(10)
                subprocess.run("shutdown -l")
            if shutdownTime !=0:
                if shutdownTime < time.time() and openShutdownTime < time.time():
                    if repetition == 1:
                        database.changeTime((shutdownTime + 86400), (openShutdownTime + 86400), 1, 0)
            print(int(shutdownTime - time.time()))      
            if int(shutdownTime - time.time()) ==300: notify.FiveMinutes()
        
            time.sleep(1)
        
    except:
        print("CLOCK ERROR")
        time.sleep(5)