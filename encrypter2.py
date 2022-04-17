import random


def encriptar(encript):
    global result
    text = str(encript)
    
    x = int(random.uniform(0, 9))
    
    sol = ""
    sol3 = []
    
    for i in text:
         y = ord(i)
         sol = sol+str(y+x)+"."
    sol = sol+str(x)
    
    sol2 = sol.split(".")
    
    for num in sol2:
        op = int(num)
        op = bin(op)
        sol3.append(op)
        
    return (" ".join(sol3))
    
# DESENCRIPTAR

def desencriptar(desencript):
    sol4 = []
    text = desencript
    text = text.split(" ")
    for y in text:
        op = int(y, 2)
        op = op-int(text[len(text)-1], 2)
        sol4.append(chr(op))
        
    return ("".join(sol4))