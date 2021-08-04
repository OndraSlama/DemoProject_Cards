""" 
Demo project implementing operations with deck of cards
Author: Ondrej Slama
Date: 04.08.2021
"""

from dataclasses import dataclass
import random

SUPPORTED_RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
SUPPORTED_SUITS = {"Spades", "Hearts", "Diamonds", "Clubs"}

@dataclass
class Card:
    """ Single card implementation """
    rank: str
    suit: str

    def __post_init__(self):
        if self.rank not in SUPPORTED_RANKS:
            raise ValueError(f"Rank {self.rank} not supported")
        if self.suit not in SUPPORTED_SUITS:
            raise ValueError(f"Suit {self.suit} not supported")

    def value(self) -> int:
        """ Return rank as value """
        return SUPPORTED_RANKS.index(self.rank) + 1

    def suit_as_String(self) -> str:
        """ Return suit as string """
        return self.suit

    def rank_as_string(self) -> str:
        """ Return rank as string """
        return self.rank

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


@dataclass(init=False)
class Deck():
    """ Deck implementation"""
    remaining_cards: list   
    dealt_cards: list

    def __init__(self):
        self.remaining_cards = [Card(rank, suit) for rank in SUPPORTED_RANKS for suit in SUPPORTED_SUITS]
        self.dealt_cards = []

    def shuffle(self) -> None:
        """ Shuffle deck """      
        self.remaining_cards = [*self.remaining_cards, *self.dealt_cards]
        self.dealt_cards = []
        random.shuffle(self.remaining_cards)

    def remaining(self) -> int:
        """ Return remaining cards """
        return len(self.remaining_cards)

    def deal(self) -> Card:
        """ Deal a card """
        if self.remaining() == 0:
            raise ValueError("No more cards in deck")
        card = self.remaining_cards.pop()
        self.dealt_cards.append(card)
        return card

    def __str__(self) -> str:
        return f"Deck of {len(self.remaining_cards)} cards :{[str(c) for c in self.remaining_cards]}" 

@dataclass
class Hand():
    """ Hand implementation """
    cards: list

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        """ Add a card to hand """
        if len(self.cards) == len(SUPPORTED_SUITS) * len(SUPPORTED_RANKS):
            raise ValueError("Hand already has maximum number of cards")

        self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        """ Remove a card from hand """
        if len(self.cards) == 0:
            raise ValueError("No cards in hand")

        if card not in self.cards:
            raise ValueError(f"Card {card} not in hand")

        self.cards.remove(card)

    def sort_by_suit(self) -> None:
        """ Sort hand by suit """
        self.cards.sort(key=lambda c: c.suit)
        self.sort_by_value()

    def sort_by_value(self) -> None:
        """ Sort hand by value """
        self.cards.sort(key=lambda c: c.value())



    def __str__(self) -> str:
        return f"Hand of {len(self.cards)} cards :{[str(c) for c in self.cards]}" 

        
        



def main():

    #----------------------------- Basic tests -----------------------------
    # Card test
    card = Card("Ace", "Spades")
    assert card.value() == 1
    assert card.suit_as_String() == "Spades"
    assert card.rank_as_string() == "Ace"
    assert str(card) == "Ace of Spades"    
    
    # Deck tests
    deck = Deck()
    assert deck.remaining() == 52

    deck.deal()
    assert deck.remaining() == 51
    assert len(deck.dealt_cards) == 1
    

    deck.shuffle()
    assert deck.remaining() == 52

    try:
        for _ in range(len(SUPPORTED_SUITS) * len(SUPPORTED_RANKS) + 1):
            deck.deck.deal()
    except ValueError:
        print("Exception raised correctly")
    else:
        assert False, "Should have raised exception (no cards in deck)"

    # Hand tests
    deck.shuffle()
    hand = Hand()
    assert len(hand.cards) == 0
    
    for _ in range(5):
        hand.add_card(deck.deal())
    assert len(hand.cards) == 5

    hand.remove_card(hand.cards[0])
    assert len(hand.cards) == 4

    
    deck.shuffle()

    try:
        for _ in range(len(SUPPORTED_SUITS) * len(SUPPORTED_RANKS)):
            hand.add_card(deck.deal())
    except ValueError:
        print("Exception raised correctly")
    else:
        assert False, "Should have raised exception (too many cards in hand)"


if __name__ == "__main__":
    main()