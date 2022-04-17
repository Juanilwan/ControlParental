import json, hashlib, random

def getTime() -> int:  
    with open('data.json','r+') as json_file:
        data = json.load(json_file)
        if 'shutdownTime' not in data:
            data['shutdownTime'] = 0
            json.dump(data, json_file)
            json_file.close()
        return data['shutdownTime']
    
def getOpenTime() -> int:  
    with open('data.json','r+') as json_file:
        data = json.load(json_file)
        if 'openShutdownTime' not in data:
            data['openShutdownTime'] = 86400
            json.dump(data, json_file)
            json_file.close()
        return data['openShutdownTime']

def changeTime(n: int, m: int, o: int):
    with open('data.json','w') as json_file:
        data = { "shutdownTime": n, "openShutdownTime": m, "repeat": o}
        json.dump(data, json_file)

        
def IRepeat() -> int:  
    with open('data.json','r+') as json_file:
        data = json.load(json_file)
        if 'repeat' not in data:
            data['repeat'] = 0
            json.dump(data, json_file)
            json_file.close()
        return data['repeat']

# Dejamos de dar soporte a encrypt, empezamos a usar la funcion password de database.py
def encrypt(x, y, z):
    m = hashlib.md5(bytes(x.encode(encoding='UTF-8'))).hexdigest()
    if y != 0:
        with open('password.json','w') as json_file:
            data = {"passwords": m, "mail": z}
            json.dump(data, json_file)
    return m
        
def getPassword():
    with open('password.json','r+') as json_file:
        data = json.load(json_file)
        return data['passwords']
    
def getMail():
    with open('password.json','r+') as json_file:
        data = json.load(json_file)
        return data['mail']
    
def changeMail(x, y):
    with open('password.json','w') as json_file:
        data = { "passwords": y, "mail": x}
        json.dump(data, json_file)
    
def getWebs():
    web_list = []
    with open('website.json','r+') as jsonFile:
        data = json.load(jsonFile)
        web_list.append(data['websites'])
        return web_list
        

def changeWebs(n: str):
    x = getWebs()
    if n == "": pass
    elif x[0] == '':
        y = x[0]+str(n)
        with open('website.json','w') as json_file:
            data = {"websites": y}
            json.dump(data, json_file)
        return y
    else:
        y = x[0]+','+str(n)
        with open('website.json','w') as json_file:
            data = {"websites": y}
            json.dump(data, json_file)
        return y
    
def clear_weblist():
    with open('website.json','w') as json_file:
        nothing = ''
        data = { "websites": nothing}
        json.dump(data, json_file)
        print("Removed")
        
def getID():
    with open('id.json','r+') as json_file:
        data = json.load(json_file)
        return [data['deviceid'], data['userid']]

def getMaxTime():
    with open('timer.json','r+') as json_file:
        data = json.load(json_file)
        return data['maxTime']
    
def getResetTime():
    with open('timer.json','r+') as json_file:
        data = json.load(json_file)
        return data['resetTime']
    
def setdeviceID(x: str):
    with open('id.json','w') as json_file:
        data = {"deviceid": x, "userid": getID()[1]}
        json.dump(data, json_file)
        
def setID(x: str, y: str):
    with open('id.json','w') as json_file:
        data = {"deviceid": x, "userid": y}
        json.dump(data, json_file)

def getWifi():
    with open('wifi.json','r+') as json_file:
        data = json.load(json_file)
        return data['activated']
    
def genPassword():
    let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    ch = random.choice([True, False])
    
    pas = ""
    num = 0
    
    while num != 5:
        if ch: pas = pas+random.choice(let)
        else: pas = pas+str(random.randrange(0, 9))
        num +=1
        ch = random.choice([True, False])
        if num == 5: return pas