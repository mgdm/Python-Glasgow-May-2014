from random import shuffle

def hand_value(hand):
    r = 0
    for c in hand:
        r += c[1]

    return r

class Deck:

    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def __init__(self, shuffle_func=None):
        self.cards = []

        if shuffle_func is None:
            self.shuffle_func = shuffle
        else:
            self.shuffle_func = shuffle_func

        for s in self.suits:
            for v in self.values:
                self.cards.append((s, v))

    def shuffle(self):
        self.shuffle_func(self.cards)
        
    def deal(self):
        return self.cards.pop(0)

class Game:

    def __init__(self, player_hands):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer_hand = []

        self.player_hands = []
        for i in range(0, player_hands):
            self.player_hands.append([])

    def initial_deal(self):
        self._deal_players()
        self.dealer_hand.append(self.deck.deal())
        self._deal_players()

    def play(self):
        pass

    def _deal_players(self):
        for hand in self.player_hands:
            hand.append(self.deck.deal())


if __name__ == '__main__':
    players = 4

    game = Game(players)
    game.initial_deal()

    for i in range(0, players):
        print "Player %d has %d" % (i + 1, hand_value(game.player_hands[i]))

    print "Dealer has %d" % hand_value(game.dealer_hand)
