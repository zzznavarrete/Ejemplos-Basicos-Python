import turtle

#Obligatorio en python
def main():
    window = turtle.Screen()
    chica = turtle.Turtle()
    
    make_square(chica)
    
    
    
def make_square(chica):
    length = int(input('Tamaño de cuadrado:'))
    for i in range(4):
        make_line_and_turn(chica, length)
    


def make_line_and_turn(chica, length):
    chica.forward(length)
    chica.left(90)
    

#Esto es el constructor de python
if __name__ == '__main__':
    main()