import unittest

import copy

from blackjack import Deck

def shuffle_func(list):
    first_card = list[0]
    last_card = list[51]

    list[0], list[51] = last_card, first_card

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_cards(self):
        self.assertEqual(52, len(self.deck.cards))

    def test_shuffle(self):
        cards_before = list(self.deck.cards)
        self.deck.shuffle(shuffle_func)
        cards_after = list(self.deck.cards)

        self.assertNotEqual(cards_before, cards_after)

    def test_deal(self):
        expected = self.deck.cards[51]
        card = self.deck.deal()

        self.assertEqual(expected, card)

if __name__ == '__main__':
    unittest.main() 
