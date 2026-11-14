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
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
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

#bubble sorter method that i made from an AP compsci class and remade into python
def sort_hand(hand):
    swap_counter = 1
    while (swap_counter != 0):
        swap_counter = 0

        for(card in hand[:-1]):
            if (card.rank > card+1.rank):
                temp = card
                card = card+1
                card+1 = temp

                swap_counter += 1

    return hand


def poker_classification(hand):
    # Returns a string describing the poker hand. First, validate the input
    # to make sure it is a set of 5 cards, and raise the appropriate error
    # (TypeError or ValueError) if necessary.
    #
    # Then return one of the following strings:
    # "High Card", "One Pair", "Two Pair", "Three of a Kind",
    # "Straight", "Flush", "Full House", "Four of a Kind",
    # "Straight Flush", "Royal Flush"
    #
    # Make sure to remove this comment and the pass statement below
    # before submitting.

    for card in hand:
        if not isinstance(card, Card) or not isinstance(hand, set):
            raise TypeError("hand should be a set of Cards")
    if len(hand) != 5:
        raise ValueError("hand should contain 5 Cards")

    
    
