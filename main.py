from dataclasses import dataclass

SUPPORTED_RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
SUPPORTED_SUITS = {"Spades", "Hearts", "Diamonds", "Clubs"}

@dataclass
class Card:
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



def main():
    card = Card("Ace", "Spades")

    print(card)

if __name__ == "__main__":
    main()