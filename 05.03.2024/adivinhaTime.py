import os
import time

times = [
    "Arsenal",
    "Atlético de Madrid", 
    "Barcelona", 
    "Bayern", 
    "Dortmund",
    "FC Porto", 
    "Inter", 
    "Lazio", 
    "Leipzig",
    "Manchester City",
    "Napoli",
    "Paris Saint-Germain",
    "PSV", 
    "Real Madrid",
    "Real Sociedad", 
    "Sevilla"
]

print("bem Vrindo ao jogo da adivinhação! ")
time.sleep(3)
print("Tente adivinhar 3 times da champions  ")

def jogo(times):
    
    pontos = 0
    
    for x in range(3):
        # palpite = input("Digite um time: ").capitalize().strip()
        palpite = input("Digite um time: ")
        
        # islower() minuscula
        # isupper() maiuscula
        # olhar a implementação usando esses metodos, verificar se é tudo maiuscula e usar o capitalize 

        
        if palpite in times and not palpite.isupper():
                palpite= palpite.capitalize()
                pontos += 1
                os.system("cls")
                print(f'Parabens vc acertou um time! Você tem {pontos} pontos')
                times.remove(palpite)
                    
        else:
            os.system("cls")
            print(f'Este time não está na lista.  Você tem {pontos} pontos')
            
            
jogo(times)