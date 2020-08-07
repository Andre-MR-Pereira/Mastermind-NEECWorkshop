from functions import *
from board import *
from os import system

def game():
    system('clear')
    tabuleiro=Board()
    tabuleiro.printBoard()
    for iteration in range(8):
        attempt=generateInput()
        info=tabuleiro.Guess(attempt,iteration)
        print(info)
        if info==True or iteration==7:
            tabuleiro.printResult(info)
            break

game()
