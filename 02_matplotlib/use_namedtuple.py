import collections

Cards = collections.namedtuple('Cards',['rank','suit'])
class FrenchDeck:
    ranks = [str(_) for _ in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Cards(rank,suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

deck = FrenchDeck()
print(len(deck))
from random import choice
print(choice(deck))

for card in deck._cards:
    print(card)

suit_value = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = deck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]

for card in sorted(deck,key=spades_high,reverse=True):
    print(card)
