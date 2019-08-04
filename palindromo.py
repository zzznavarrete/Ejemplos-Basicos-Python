
def palindromo2(palabra):
    palabra_revertida = palabra[::-1]
    
    if palabra_revertida == palabra:
        return True
    else:
        return False
    
    

def palindromo(palabra):
    palabra_revertida = []

    for letra in palabra:
        palabra_revertida.insert(0, letra)
    
    revertida = ''.join(palabra_revertida)
    
    if revertida == palabra:
        return True
    else:
        return False
    
    

if __name__ == '__main__':
    palabra = str(input('Escribe una palabra: '))
    
    result = palindromo2(palabra)
    
    if result:
        print('{} sí es un palíndromo'.format(palabra))
    else:
        print('{} NO es un palíndromo '.format(palabra))
        
        
    
    