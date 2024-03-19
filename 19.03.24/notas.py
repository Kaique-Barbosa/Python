import customtkinter as ctk

# funcoes
def formula():
    n1 = float(nota1.get())
    n2 = float(nota2.get())
    n3 = float(nota3.get())
    
    media = (n1 +n2 +n3) / 3
    if(media >= 7):
        resultado.configure(text=f'sua media foi: {media:.1f} \n você foi aprovado! ')
    else:
        resultado.configure(text=f'sua media foi: {media:.1f} \n você foi de recu! ')
    
def limpar():
    nota1.delete(0,'end')
    nota2.delete(0,'end')
    nota3.delete(0,'end')
    resultado.configure(text='')
#  ------------



ctk.set_appearance_mode('dark')

janela = ctk.CTk()

janela.minsize(600,400)
janela.title("Sistema escolar V 1.0")

ctk.CTkLabel(janela, text='Sistema escolar --V 1.0', text_color='darkgreen', font=('arial', 27, 'bold')).pack(pady=5)

nota1 = ctk.CTkEntry(janela, placeholder_text="digite a nota da 1º unidade", width=400, height=30)
nota1.pack(pady=5)
nota2 = ctk.CTkEntry(janela, placeholder_text="digite a nota da 2º unidade", width=400, height=30)
nota2.pack(pady=5)
nota3 = ctk.CTkEntry(janela, placeholder_text="digite a nota da 3º unidade", width=400, height=30)
nota3.pack(pady=5)

btn = ctk.CTkButton(janela,text='Calcular', fg_color='green', text_color='white', width=100, height=30, border_width=1, cursor="heart", command=formula)
btn.pack(pady=10)

btnLimpar = ctk.CTkButton(janela,text='Limpar', fg_color='darkblue', text_color='white', width=100, height=30, border_width=1, cursor="heart", command=limpar)
btnLimpar.pack(pady=10)

resultado = ctk.CTkLabel(janela, text='', font=('arial', 40, 'bold'), text_color='white')
resultado.pack(pady=5, padx=50)


janela.mainloop()
