numeros = [10, 20, 30, 40, 50]

def media(numeros):
    
    quantidade = len(numeros)
    somatorio = sum(numeros)
    resultado = somatorio / quantidade
    
    return resultado

def imprimir():

    return print(f'A media do vetor é:  { media(numeros)}')

imprimir()    
    
    
    