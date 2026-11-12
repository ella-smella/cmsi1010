from dataclasses import dataclass
from random import shuffle

@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"

def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]

def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards

def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])

def deal(number_of_hands, cards_per_hand):
    deck = shuffled_deck()
    hands = []
    if not isinstance(number_of_hands, int) or not isinstance(cards_per_hand, int):
        raise TypeError("number of hands and number of cards must be an integer")
    
    if number_of_hands <= 0 or cards_per_hand <= 0:
        raise ValueError("number of hands and number of cards must be positive")

    if number_of_hands * cards_per_hand > 52:
        raise ValueError("required amount of cards exceeds the number of cards in a standard deck")

    hand_start = 0
    hand_end = cards_per_hand
    for i in range(1, number_of_hands + 1):
        hands.append(set(deck[hand_start:hand_end]))
        hand_start = hand_end
        hand_end += cards_per_hand 

    return hands
    #for loop of the amount of number of hands
    #do the deal one five card hand code, but obvi replace the 5 with cards per hand
    #create another hand but start off from 1 + the cards per hand, make that a value and +=


for hand in deal(5, 5):
    for card in hand:
        print(card, end=' ')
    print()
