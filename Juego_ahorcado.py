import os
import random
from colorama import Back, Fore, init


ahorcado_image_ascci = """

                       .-'''-.                   _..._                               .-'''-.     
                      '   _    \              .-'_..._''.           _______         '   _    \   
            .       /   /` '.   \           .' .'      '.\          \  ___ `'.    /   /` '.   \  
          .'|      .   |     \  '          / .'                      ' |--.\  \  .   |     \  '  
         <  |      |   '      |  '.-,.--. . '                        | |    \  ' |   '      |  ' 
    __    | |      \    \     / / |  .-. || |                 __     | |     |  '\    \     / /  
 .:--.'.  | | .'''-.`.   ` ..' /  | |  | || |              .:--.'.   | |     |  | `.   ` ..' /   
/ |   \ | | |/.'''. \  '-...-'`   | |  | |. '             / |   \ |  | |     ' .'    '-...-'`    
`" __ | | |  /    | |             | |  '-  \ '.          .`" __ | |  | |___.' /'                 
 .'.''| | | |     | |             | |       '. `._____.-'/ .'.''| | /_______.'/                  
/ /   | |_| |     | |             | |         `-.______ / / /   | |_\_______|/                   
\ \._,\ '/| '.    | '.            |_|                  `  \ \._,\ '/                             
 `--'  `" '---'   '---'                                    `--'  `"                              
"""


def compare(letter,chosen_word, guess ):
    if letter in chosen_word:
        for i,x in enumerate(chosen_word):
            if x == letter:
                guess.insert(i, x)
                guess.pop(i + 1)
    return guess


def run():
    init()
    os.system("cls")
    with open("./archivos/data.txt", "r", encoding= "utf-8") as word:
        words_list = [i for i in word]
    guess = []
    run = True
    chosen_word = list(words_list[random.randint(0, len(words_list) - 1)])
    chosen_word.pop(len(chosen_word) - 1)
    lives = len(chosen_word) + 5
    for i in chosen_word:
            guess.append("-")
    while run:
        if chosen_word != guess and lives > 0:
            os.system("cls")
            print(Back.RED + Fore.BLACK + ahorcado_image_ascci + Fore.RESET + Back.RESET)
            print(Fore.RED + "".join(guess) + "      " + str(lives) + "\u2764")
            chosen_letter = input("Escribe una letra: ")
            compare(chosen_letter, chosen_word, guess)
            lives -= 1
        elif chosen_word == guess:
            print("felicitaciones ganaste")
            print("La palabra era " + "".join(guess))
            try:
                play = int(input("Quieres volver a jugar?: \n (1)Si (2)No, salir    "))
            except ValueError:
                print("Sea serio")
                play = 2
            if play == 1:
                chosen_word = list(words_list[random.randint(0, len(words_list) - 1)])
                chosen_word.pop(len(chosen_word) - 1)
                lives = len(chosen_word) + 5
                guess = []
                for i in chosen_word:
                    guess.append("-")
            elif play == 2: 
                run = False
            else:
                play
        else:
            print("perdiste")
            print("La palabra era " + "".join(guess))
            print("".join(chosen_word))
            try:
                play = int(input("Quieres volver a jugar?: \n (1)Si (2)No, salir   "))
            except ValueError:
                print("Sea serio")
                play = 2
            if play == 1:
                chosen_word = list(words_list[random.randint(0, len(words_list) - 1)])
                chosen_word.pop(len(chosen_word) - 1)
                lives = len(chosen_word) + 5
                guess = []
                for i in chosen_word:
                    guess.append("-")
                
            elif play == 2: 
                run = False
            else:
                play


if __name__ == '__main__':
    run()