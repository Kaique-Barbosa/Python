import os
import random

secreto = random.randint(1,100) 

tentativas = 1

while True:
    palpite = int(input("Digite um numero entre 1 e 100: \n"))
    os.system("cls")
    if palpite == secreto:
        print(f"Parabéns vc acertou o numero secreto em {tentativas} tentativas")
        break
    elif palpite < secreto:
        print("O numero secreto é MAIOR que o digitado")
        tentativas+=1
    elif palpite > secreto:
        print("O numero secreto é MENOR que o digitado")
        tentativas+=1
    
