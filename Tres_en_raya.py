import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

def def_player1():
    print("Decide con que jugar. ¿O o X?")
    choice = input()
    if choice == 'X' or choice == 'x':
        print("Eres X. ¡Buena suerte!")
        player1 = 1
        return (player1)
    elif choice == 'O' or choice == 'o':
        print("Eres O. ¡Buena suerte!")
        player1 = 2
        return (player1)
    else:
        print("Formato invalido, intenta de nuevo.")
        def_player1()

def ask_position():
        print("Introduce las coordenadas con espacio")
        try :
                pos = list((input()).replace(',',' ').strip('()').split())
                pos_y = int(pos[0])
                pos_x = int(pos[1])
                if (0 <= pos_x < 3) and (0 <= pos_y < 3):
                        return([pos_y,pos_x])
                else :
                        print("Numeros invalidos")
                        return ask_position()
        except:
                print("Formato invalido, intenta de nuevo.")
                return ask_position()

def game_grid(my_matrix):
    fig, ax = plt.subplots(figsize=(3,3)) #Aqui creamos la figura con matplotlib
    ax.hlines([0, 1, 2, 3], 0, 3, lw=1)
    ax.vlines([0, 1, 2, 3], 0, 3, lw=1)
    ax.set_xticks([])
    ax.set_yticks([])
    trans = Affine2D().translate(0.5, 0.5) + ax.transData
    y = 0
    while y < my_matrix.shape[0]:
        x = 0
        while x < my_matrix.shape[1]:
            if my_matrix[y][x] == 1:
                 ax.text(x, 2-y, 'X', ha='center', va='center', fontsize=40, color='green', transform=trans)
            elif my_matrix[y][x] == 2:
                ax.text(x, 2-y, 'O', ha='center', va='center', fontsize=40, color='red', transform=trans)
            x += 1
        y += 1
    plt.show()

def fin_check(my_matrix):
    if np.any(np.all(my_matrix == 1, axis=1)) or np.any(np.all(my_matrix == 1, axis=0)):
        print("Gano X!")
        return (1)
    elif np.any(np.all(my_matrix == 2, axis=1)) or np.any(np.all(my_matrix == 2, axis=0)):
        print("Gano O!")
        return (1)
    elif (np.all(my_matrix.diagonal() == 1)) or (np.all(np.fliplr(my_matrix).diagonal() == 1)):
        print("Gano X!")
        return (1)
    elif (np.all(my_matrix.diagonal() == 2)) or (np.all(np.fliplr(my_matrix).diagonal() == 2)):
        print("Gano O!")
        return (1)
    elif np.all(my_matrix != 0):
        print("Fin del juego. No hay ganador!")
        return (1)

def main_game():
    if def_player1() == 1:
        player1 = 1
        player2 = 2
    else:
        player1 = 2
        player2 = 1
    my_matrix = np.zeros((3,3),dtype=int)
    n = 1
    while True:
        if n == 1:
            [y1,x1] = ask_position()
            if (my_matrix[y1,x1] == 0):
                my_matrix[y1,x1] = player1
                game_grid(my_matrix)
                n = 2
                if fin_check(my_matrix) == 1:
                    break
            else:
                print("Esta casilla esta ocupada")
                n = 1
        if n == 2:
            [y2,x2] = ask_position()
            if (my_matrix[y2,x2] == 0):
                my_matrix[y2,x2] = player2
                game_grid(my_matrix)
                n = 1
                if fin_check(my_matrix) == 1:
                    break
            else:
                print("Esta casilla esta ocupada")
                n = 2
                
def main():
    main_game()

if __name__ == '__main__':
    main()