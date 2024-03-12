import customtkinter as ct
import os

# AFUNÇÔES
def desligar():
    os.system('shutdown /s /t 0')

def reiniciar():
    os.system('shutdown /r /t 0')

def bloquear():
    os.system('shutdown /l /t 0') 


ct.set_appearance_mode('dark')

janela = ct.CTk("black")
janela.minsize(300,500)
janela.title("Bomba patch 💣💣💣")

titulo = ct.CTkLabel(janela,text="BOMBA PATCH V1.0", text_color="darkred")
titulo.pack()

btn1 = ct.CTkButton(janela,text="Desligar", fg_color="White", text_color="darkgray" ,width=200,height=200 ,command=desligar)
btn1.pack(pady=20)
btn2 = ct.CTkButton(janela,text="Reiniciar" , fg_color="White", text_color="darkgray", width=200,height=200, command=reiniciar)
btn2.pack(pady=20)
btn3 = ct.CTkButton(janela,text="bloquear" , fg_color="White", text_color="darkgray", width=200,height=200, command=bloquear)
btn3.pack(pady=20)





janela.mainloop()
