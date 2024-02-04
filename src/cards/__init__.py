"""CARDS INITALISATION."""


# CONSTANTS SETUP
SUITS = ["CLUBS", "HEARTS", "SPADES", "DIAMONDS"]
# NUM_CARDS = [52]
ROYAL_CARDS = ['JACK', 'QUEEN', 'KING', 'ACE']
NUMERICAL_CARDS = [ card for card in range(2,11) ]
ACE_INDEX = len(ROYAL_CARDS) - 1
# using 0 index for ace low card for sorting
ALL_CARDS = [ROYAL_CARDS[ACE_INDEX]] + [ card for card in range(2,11) ] + ROYAL_CARDS[:ACE_INDEX]
NUM_JOKERS = 2
MEMBER_CARDS = [NUMERICAL_CARDS, ROYAL_CARDS]

# SUITS = ("CLUBS", "HEARTS", "SPADES", "DIAMONDS")

CARDS = []
for suit in SUITS:
    # print(suit)
    # for card_list in MEMBER_CARDS:
    for card in ALL_CARDS:
        CARDS = CARDS + [f"{suit}-{card}"]

print(CARDS)

