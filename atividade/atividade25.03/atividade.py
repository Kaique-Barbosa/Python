import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as t



def calcular():
    imc = float(peso.get())/(float(altura.get())*float(altura.get()))
    mostrar.configure(text=f'Srª {nome.get()} seu IMC é: {imc:.1f}')

    if imc < 18.5:
        imagem =  ctk.CTkImage(light_image=Image.open("gotosa.jpg"), size=(300,300))
    elif imc > 18.5 and imc < 25:
        imagem =  ctk.CTkImage(light_image=Image.open("gotosa.jpg"), size=(300,300))
    else:
        imagem =  ctk.CTkImage(light_image=Image.open("gotosa.jpg"), size=(300,300))
        
        


ctk.set_appearance_mode('dark')

janela = ctk.CTk()

janela.minsize(500,300)
janela.title("Calcular IMC")

ctk.CTkLabel(janela, text="Calcula IMC:").pack(pady=10)

nome = ctk.CTkEntry(janela, placeholder_text="Digite seu nome")
nome.pack(pady = 10)

peso = ctk.CTkEntry(janela, placeholder_text="Digite seu peso")
peso.pack(pady = 10)

altura = ctk.CTkEntry(janela, placeholder_text="Digite sua altura")
altura.pack(pady = 10)


btn = ctk.CTkButton(janela, text="Calcula", command=calcular).pack(pady = 40)



imagem = ''

labelImagem = ctk.CTkLabel(janela, text="", image=imagem)
labelImagem.pack(pady= 40, padx = 100)

mostrar = ctk.CTkLabel(janela, text="", text_color="white")
mostrar.pack(pady= 40, padx = 100)


janela.mainloop()
