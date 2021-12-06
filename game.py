from functionality import *
from submit_new_users import *
from deck import *
import os

def game_menu(player):
    os.system("clear")
    print(f"{player.name} que es lo que desea hacer?")
    print(f"1- Jugar una partida")
    print(f"2- Sumar más dinero al bankroll una nueva partida")
    print(f"3- Conocer los detalles de su perfil")
    print(f"4- Salir del juego")
    choice = int(input(""))
    if choice == 1:
        pass
    elif choice == 2:
        player.more_money()
    elif choice == 3:
        print(player)
    elif choice == 4:
        sys.exit()

def play_game ():
    player1 = User()
    print(f"Bienvenido {player1.name.capitalize()}, tu bankroll es de ${player1.balance}")
    game_menu(player1)
    game_deck = make_deck()
    initial_hand_pc(game_deck)
    initial_hand_player(game_deck)
    player_score = player_turn(game_deck)
    print(player_score)

if __name__ == '__main__':
    play_game()