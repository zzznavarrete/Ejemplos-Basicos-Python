
def temperatura_promedio(temperaturas):
    suma_de_temperaturas = 0
    
    for temp in temperaturas:
        suma_de_temperaturas += temp
        
    return suma_de_temperaturas/len(temperaturas)



if __name__ == '__main__':
    temperaturas = [10, 17, 21, 18, 20, 21, 13]
    
    promedio = temperatura_promedio(temperaturas)
    
    print('La temperatura promedio es: {}'.format(promedio))
    
    