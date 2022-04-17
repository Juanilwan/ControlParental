import urllib.request
import tkinter as tk

def detectPayment(website):
    def unblock(website):
        website = website.split(".")
        
        root = tk.Tk()
        loadimage1 = tk.PhotoImage(file='moneySymbol.png')
        root.geometry("342x672+645+135")
        root.resizable(False, False)
        root.title("Jupiter Payments Protection")
        tk.Label(root, image=loadimage1).pack()
        tk.Label(root, text="Se ha detectado que esta página web permite pagos.").pack()
        tk.Label(root, text=("Página Web: "+website[1]+"."+website[2])).place(x=10, y=180)
        
        root.mainloop()
    
        
  
        
  
     
    content = urllib.request.urlopen(website)
    read_content = str(content.read())
    # print(read_content)
    points = 0
    
    var1 = read_content.split('pagar')
    var2 = read_content.split('pago')
    var3 = read_content.split('compra')
    var4 = read_content.split('pedido')
    var5 = read_content.split('carrito')
    var6 = read_content.split('producto')
    var7 = read_content.split('barat')
    var8 = read_content.split('descuento')
    var9 = read_content.split('bolsa')
    var10 = read_content.split('EUR')
    
    if len(var1)>1: points+=0.5
    if len(var2)>1: points += 0.8
    if len(var3)>1: points += 0.5
    if len(var4)>1: points +=0.8
    if len(var5)>1: points +=0.5
    if len(var6)>1: points +=0.5
    if len(var7)>1: points +=0.7
    if len(var8)>1:points +=0.7
    if len(var9)>1:points +=0.5
    if len(var10)>1:points +=0.2
    
    print(points)
    if points >=2.5: unblock(website)

detectPayment('https://www.adivin.com/')

    
    
    
    
    
    
    
    
    
    
    