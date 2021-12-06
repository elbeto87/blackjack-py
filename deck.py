import random

def make_deck ():
    deck = []
    suits = ['Corazones', 'Diamantes', 'Trébol', 'Picas']
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    for suit in suits:
        for card in cards:
            deck.append((card, suit))
    random.shuffle(deck)
    return deck