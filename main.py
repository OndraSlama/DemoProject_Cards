from dataclasses import dataclass
import dataclasses

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
    cards: list   

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in SUPPORTED_RANKS for suit in SUPPORTED_SUITS]

    def __str__(self) -> str:
        return f"Deck of {len(self.cards)} cards :{[str(c) for c in self.cards]}" 
        
        



def main():

    deck = Deck()

    print(deck)

if __name__ == "__main__":
    main()