# CONSTANTS SETUP
SUITS = ["CLUBS", "HEARTS", "SPADES", "DIAMONDS"]
ROYAL_CARDS = ['JACK', 'QUEEN', 'KING', 'ACE']
NUMERICAL_CARDS = list(map(str, range(2, 11)))
ALL_CARDS = [ROYAL_CARDS[-1]] + NUMERICAL_CARDS + ROYAL_CARDS[:-1]
NUM_JOKERS = 2
MEMBER_CARDS = [NUMERICAL_CARDS, ROYAL_CARDS]

# Generate the deck of cards
CARDS = [f"{suit}-{card}" for suit in SUITS for card in ALL_CARDS]

print(CARDS)

#Dealing 2 cards randomly

import random

def deal_cards(num_cards):
    """Deal a specified number of random cards."""
    return random.sample(CARDS, num_cards)

def main():
    print("Welcome to Backshot Roulette!")

    # Deal two random cards
    player_hand = deal_cards(2)

    print("Player's hand:", player_hand)

if __name__ == "__main__":
    main()
