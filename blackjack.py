from random import shuffle

class Deck:

    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    cards = []

    def __init__(self):
        for s in self.suits:
            for v in self.values:
                self.cards.append((s, v))

    def shuffle(self, shuffle_func):
        shuffle_func(self.cards)
        
    def deal(self):
        return self.cards.pop()
