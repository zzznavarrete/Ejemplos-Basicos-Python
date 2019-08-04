import random


_IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']


_PALABRAS = [
    'lavadora',
    'chica',
    'weed'
]

def random_word():
    id = random.randint(0, len(_PALABRAS) -1)
    return _PALABRAS[id]
 
 
def display_board(hidden_word, intentos):
     print(_IMAGES[intentos])
     print('')
     print(hidden_word)
     print('----- * ------ * ----- * ------ * ----- * ------ *')
     
    

def run():
    palabra = random_word()
    letras_ocupadas = []
    hidden_word = ['-'] * len(palabra)
    intentos = 0 
    
    while True:
        display_board(hidden_word, intentos)
        
        if len(letras_ocupadas) > 0:
            print('*********************************************')
            print('Has ocupado las siguientes letras: {}'.format(letras_ocupadas))
        
        current_letter = str(input('Escoge una letra: '))
        letras_ocupadas.append(current_letter)
        
        letter_indexes = []
        for i in range(len(palabra)):
            
            if palabra[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            
            
            
            intentos += 1
            
            if intentos == 7:
                display_board(hidden_word, intentos)
                print('')
                print('Perdiste, la palabra correcta era {}'.format(palabra))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter    

            letter_indexes  = []
            
        try:
            hidden_word.index('-')
        except ValueError:
            print('****************************************************************')
            print('FELICIDADES!, Ganaste, la palabra correcta era: [  {}  ]'.format(palabra))
            print('****************************************************************')
            break
        

if __name__ == "__main__":
    print('**********************')
    print("A H O R C A D O ")
    print('**********************')
    run()
    




