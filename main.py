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

    def suitAsString(self) -> str:
        """ Return suit as string """
        return self.suit

    def rankAsString(self) -> str:
        """ Return rank as string """
        return self.suit

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

    def shuffle(self):
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
        
        



def main():

    deck = Deck()
    assert deck.remaining() == 52

    deck.deal()
    assert deck.remaining() == 51
    assert len(deck.dealt_cards) == 1

    deck.shuffle()
    assert deck.remaining() == 52


if __name__ == "__main__":
    main()