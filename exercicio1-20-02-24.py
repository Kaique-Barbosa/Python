import os

nome = input("Digite seu nome: ")
uni1 = float(input("Digite sua 1º nota: "))
uni2 = float(input("Digite sua 2º nota: "))
uni3 = float(input("Digite sua 3º nota: "))

media = (uni1+ uni2 + uni3) / 3

if media >= 7 :
    print(f'{nome}, sua media foi: {media:.1f}')
    print("Parabens zeruella")
elif media == 5 and media < 7:
    print(f'{nome}, sua media foi: {media:.1f}')
    print("foi pra recu")
else: 
    print(f'{nome}, sua media foi: {media:.1f}')
    print("perdeu")
