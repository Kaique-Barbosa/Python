import os
# for x in range(30):
#     print("LOma")
    
# pessoas = ['Kaique','Paloma - tchan','Gisele','Lucas','gegeu','Léo']

# for x in range(len(pessoas)):
#     if pessoas[x].startswith('L'):
#         print(pessoas[x])


# for x in pessoas:
#     if x.startswith('L'):
#         print(x)

#3º armazenar os numeros dentro de 2 vetores e depois exibir esses nunmeros
    
# 1º
# valor = []
# positivo =[]
# negativo = []

# for x in range(10):
#    valor.append(int(input("digite um valor: ")))
   
    # if x >= 0:
    #     positivo.append(x)
    # else:
    #     negativo.append(x)
        
    
# print("Positivos: ", positivo)
# print("Negativos: ", negativo)
    
 # 2º ----------------------------------------------------
 
valores = [22,33,44,23,26,29,67,56,45,46,32,11,17]   
par = []
impar = []

for x in valores:
    if x %2 == 0:
        par.append(x)
    else:
        impar.append(x)
    
        
print(f"Numeros pares: {par}")        
print(f"Numeros impares: {impar}")   
print(f"A soma do vetor é:  {sum(valores)}")     
print(f"A media do vetor é:  {sum(valores) / len(valores):.2f}")     
         