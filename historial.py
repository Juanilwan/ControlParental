from browser_history import get_history
import os, timeH, ctypes


def generate():
    if timeH.getID()[0] == timeH.getID()[1]:
        outputs = get_history()
        outputs = outputs.histories
        web_list = []
        final_list = []
        for web in outputs:
            try:
                process = str(web)
                process = process.split("Romance Standard Time')), '")
                x = process[1]
                x = x.split("')")
                web_list.append(x[0])
            except: pass

        web_list.reverse()
        num = 0
        
        for web2 in web_list:
            if num <=50:
                final_list.append(web2)
                num+=1
        file = open("historial.txt", "w")
        
        file.write("Atención: La lista de páginas web está ordenada desde las más recientes a las menos recientes."+"\n")
        file.write("\n")
        for data in final_list:
            file.write("\n")
            file.write(data+"\n")
            file.write("\n")
        file.close()
        
        os.system('historial.txt')
    else: 
        ctypes.windll.user32.MessageBoxW(0, "Esta función solo esta disponible en dispositivos vinculados a tu cuenta", "¡Aviso Importante!")