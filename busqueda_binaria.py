
def binary_search(numbers, number_to_find, init, end):
    if init > end:
        return False
    
    mid =int((init + end)/2)
    #Imprimiendo las mitades de la litsta según avance
    #print(mid)
    if numbers[mid] == number_to_find:
        return True
    
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, init, mid - 1 )
    else:
        return binary_search(numbers, number_to_find, mid + 1 , end - 1 )
    
    


if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,9,10,11,25,27,28,29,34]
    
    number_to_find = int(input('Ingresa un numeo: '))
    
    resultado = binary_search(numbers, number_to_find,0, int(len(numbers) - 1)) 
    
    if resultado:
        print('El número sí está en la lista')
    else:
        print('El número NO está en la lista')