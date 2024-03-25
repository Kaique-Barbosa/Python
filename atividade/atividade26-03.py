import customtkinter as ctk


def calculoConsumo():
    dist = float(distancia.get())
    con = float(consumo.get())
    pre = float(preco.get())
    
    resultado = (dist/con)*pre
    mostrarResultado.configure(text=f'Sua media de gasto para essa viagem é de: \n R$ {resultado:.1f} ')



ctk.set_appearance_mode("dark")

janela = ctk.CTk()

janela.minsize(600,500)
janela.title("Calculadora Gasolina x Viagem")

ctk.CTkLabel(janela, text="Gasolina x Viagem", text_color="lightgreen", font=("arial", 30, "bold")).pack(pady=50)
distancia = ctk.CTkEntry(janela, placeholder_text="Digite a distancia da viagem", width=400, height=40)
distancia.pack(pady=20)
consumo = ctk.CTkEntry(janela, placeholder_text="Digite o consumo médio do carro", width=400, height=40)
consumo.pack(pady=20)
preco = ctk.CTkEntry(janela, placeholder_text="Digite o preço do combustivel", width=400, height=40)
preco.pack(pady=20)

btn = ctk.CTkButton(janela, text="Calcular", text_color="white", width=140,
                    height=40, border_width=1, border_color="lightgray", cursor="hand1", command=calculoConsumo).pack(pady=20)

mostrarResultado = ctk.CTkLabel(janela, text='', font=('arial', 20, 'bold'), text_color='white')
mostrarResultado.pack(pady=15, padx=50)

janela.mainloop()