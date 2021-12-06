from random import shuffle
from submit_new_users import User
import os
import sys

pc_deal = []
player_deal = []
player_lose = False

def initial_hand_pc(deck):
    card_pc, suit_pc = deck.pop()
    pc_deal.append((card_pc, suit_pc))
    print(f"\nA la PC le ha tocado la carta {card_pc} de {suit_pc}")
    print("Tiene otra carta tapada")
    return deck


def initial_hand_player(deck):
    card_player, suit_player = deck.pop()
    player_deal.append((card_player, suit_player))
    print(f"\nTu primer carta es un {card_player} de {suit_player}")
    print("También tienes otra carta tapada")
    return deck


def player_turn(deck):
    score_player = 0
    global player_lose
    print("\nVamos a dar vuelta la carta tapada")
    take_card_player(deck)
    while True:
        sum_cards = calculate_deal(player_deal)
        print(f"El valor total de tus cartas es de {sum_cards}")
        if sum_cards > 21:
            print("Perdiste!")
            player_lose = True
            return score_player
        elif sum_cards == 21:
            print("Felicitaciones, hiciste 21!, ahora le toca a la PC")
            score_player = 21
            return score_player
        else:
            print("Qué desea hacer?")
            print("\n1- Otra carta")
            print("2- Plantarse")
            answer = input("\n")
            if answer == '1':
                take_card_player(deck)
            else:
                score_player = sum_cards
                return score_player

def pc_turn(deck, player_score):
    if player_lose == False:
        score_pc = 0
        print("\nVamos a dar vuelta la carta tapada que tenía la PC")
        take_card_pc(deck)
        while True:
            sum_cards = calculate_deal(pc_deal)
            print(f"\nEl valor total de las cartas de la PC es de {sum_cards}")
            if sum_cards > 21:
                print("La PC ha perdido!")
                return score_pc
            elif sum_cards == 21:
                print("La PC ha ganado!")
                score_pc = 21
                return score_pc
            else:
                if sum_cards < player_score:
                        take_card_pc(deck)
                else:
                    score_pc = sum_cards
                    return score_pc

def take_card_player(partial_deck):
    card_player, suit_player = partial_deck.pop()
    print(f"Se descubre la carta y es un {card_player} de {suit_player}")
    player_deal.append((card_player, suit_player))

def take_card_pc(partial_deck):
    card_pc, suit_pc = partial_deck.pop()
    print(f"Se descubre la carta y es un {card_pc} de {suit_pc}")
    pc_deal.append((card_pc, suit_pc))

def calculate_deal(player_deal):
    total_value = 0
    for cards in range(len(player_deal)):
        if 10 == player_deal[cards][0] or 'J' == player_deal[cards][0] or 'Q' == player_deal[cards][0] or 'K' == player_deal[cards][0]:
            if (total_value > 21) and ('A' in player_deal):
                continue
            else:
                total_value = total_value + 10
        elif 'A' == player_deal[cards][0]:
            if total_value > 10:
                total_value = total_value + 1
            else:
                total_value = total_value + 11
        else:
            total_value = total_value + player_deal[cards][0]
    return total_value