import os

nome = input("Digite seu nome: ")
os.system('cls')
peso = float(input("Seu peso: "))
os.system('cls')
altura = float(input("Digite sua altura: "))
os.system('cls')


imc = peso/(altura**2)

if imc < 16.9 :
    print(f'{nome}, seu imc foi: {imc:.1f}. Está muito abaixo do peso')
elif imc >= 17 and imc <=18.4:
    print(f'{nome}, seu imc foi: {imc:.1f}. Está abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print(f'{nome}, seu imc foi: {imc:.1f}. peso normal')
elif imc >= 25 and  imc <= 29.9:
    print(f'{nome}, seu imc foi: {imc:.1f}. acima do peso')
elif imc >= 30 and  imc <= 34.9:
    print(f'{nome}, seu imc foi: {imc:.1f}. Obesidade Grau 1')
elif imc >= 35 and  imc <= 40:
    print(f'{nome}, seu imc foi: {imc:.1f}. Obesidade Grau 2')
elif imc > 40:
    print(f'{nome}, seu imc foi: {imc:.1f}. Obesidade Grau 3')


    
