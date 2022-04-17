import time, subprocess, notify, calendar, database, timeH

d = time.strftime("%d", time.localtime(time.time()))
m = time.strftime("%m", time.localtime(time.time()))
y = time.strftime("%y", time.localtime(time.time()))
oHour = str(int(calendar.timegm(time.strptime(f'2022-{m}-{d} 00:00:00', '%Y-%m-%d %H:%M:%S')))+79200)
print(oHour)
log = None

while True:
    try:
        if timeH.getID()[0] != "Unconnected":
            #database.getActualTime(0)
            if log == None: actualTime = database.getActualTime(0)+1
            else:
                x = time.time()-log
                actualTime = database.getActualTime(0)+ x
    
            maxTime = database.getMaxTime(0)
            resetTime = database.getResetTime(0)
    
            if time.time()> database.getResetTime(0):
                d = time.strftime("%d", time.localtime(time.time()))
                m = time.strftime("%m", time.localtime(time.time()))
                oHour = str(int(calendar.timegm(time.strptime(f'2022-{m}-{d} 00:00:00', '%Y-%m-%d %H:%M:%S')))+79200)
                database.setTimer(0, maxTime, int(oHour), 0)
                
                actualTime = database.getActualTime(0)+1
                resetTime = database.getResetTime(0)
            else: database.setTimer(actualTime, maxTime, resetTime, 0)
            print(actualTime, maxTime)
            
            if actualTime > maxTime: 
                notify.notify()
                time.sleep(10)
                subprocess.run("shutdown -l")
                
                
            if (maxTime-actualTime) == 300:
                notify.FiveMinutes()
                
            log = time.time()
            time.sleep(0.75)
    except:
        print("Error")
        time.sleep(5)