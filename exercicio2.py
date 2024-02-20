import os

nome = input("Digite o seu nome: ")
os.system('cls')

valor01 = float(input("Digite o primeiro numero: "))
os.system('cls')
valor02 = float(input("Digite o segundo numero: "))
os.system('cls')
valor03 = float(input("Digite o terceiro numero: "))
os.system('cls')

# operacao = input("Escolha uma operação: * | - | + | /")
calculo = valor01 * valor02

print(f"Olá {nome}. O resultado do calculo é: {int(calculo)}")


