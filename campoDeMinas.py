import ctypes, win32con
from tkinter import filedialog as f
import tkinter as tk

def set(file): ctypes.windll.user32.SystemParametersInfoW(20, 0, file, 0)

def get(): 
    ubuf = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
    return ubuf.value

root = tk.Tk()
url_file = f.askopenfilename(initialdir = ".Desktop", filetype = ((
            "Imágenes","*.jpg" 
            ),), title = "Abrir archivo/")
root.destroy()

if url_file !="": set(url_file)

root.mainloop()

# import ctypes, win32con, time

# file = r"C:\Users\User\Desktop\SecurityManagementSystem\wallpaper.jpg"

# def get(): 
#     ubuf = ctypes.create_unicode_buffer(512)
#     ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
#     return ubuf.value

# def set(file): ctypes.windll.user32.SystemParametersInfoW(20, 0, file, 0)

# while True:
#     if get() != file:
#         print("ERROR")
#         set(file)
    
#     time.sleep(5)