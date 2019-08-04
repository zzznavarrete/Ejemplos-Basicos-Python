
def run():
    number = int(input("Escribe un número: "))
    if es_primo(number):
        print("Es primo")
    else:
        print("No es primo")
    


def es_primo(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
           
    return True
            
    


if __name__ == '__main__':
    run()