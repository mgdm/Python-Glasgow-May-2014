import unittest
import copy

from blackjack import Deck, Game, hand_value

def shuffle_func(list):
    first_card = list[0]
    last_card = list[51]

    list[0], list[51] = last_card, first_card

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck(shuffle_func)

    def test_cards(self):
        self.assertEqual(52, len(self.deck.cards))

    def test_shuffle(self):
        cards_before = list(self.deck.cards)
        self.deck.shuffle()
        cards_after = list(self.deck.cards)

        self.assertNotEqual(cards_before, cards_after)

    def test_deal(self):
        expected = self.deck.cards[0]
        card = self.deck.deal()

        self.assertEqual(expected, card)

    def test_deal_card_gone(self):
        card = self.deck.deal()
        self.assertEqual(51, len(self.deck.cards))


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_hands = 4
        self.game = Game(self.player_hands)
   
    def test_deck(self):
        self.assertEqual(self.game.deck.__class__, Deck)

    def test_player_hands(self):
        self.game.initial_deal()
        self.assertEqual(self.player_hands, len(self.game.player_hands))
        for hand in self.game.player_hands:
            self.assertEqual(2, len(hand))

    def test_dealer_hand(self):
        self.game.initial_deal()
        self.assertEqual(1, len(self.game.dealer_hand))

    def test_initial_deal(self):
        dealt_cards = self.game.deck.cards[0:9]
        
        self.game.initial_deal()

        self.assertEqual(dealt_cards[0], self.game.player_hands[0][0])
        self.assertEqual(dealt_cards[1], self.game.player_hands[1][0])
        self.assertEqual(dealt_cards[2], self.game.player_hands[2][0])
        self.assertEqual(dealt_cards[3], self.game.player_hands[3][0])
        self.assertEqual(dealt_cards[4], self.game.dealer_hand[0])
        self.assertEqual(dealt_cards[5], self.game.player_hands[0][1])
        self.assertEqual(dealt_cards[6], self.game.player_hands[1][1])
        self.assertEqual(dealt_cards[7], self.game.player_hands[2][1])
        self.assertEqual(dealt_cards[8], self.game.player_hands[3][1])


class TestHandValue(unittest.TestCase):
    def test_value_of_hand(self):
        result = hand_value([('hearts', 1), ('diamonds', 4), ('clubs', 10), ('clubs', 6)])
        self.assertEqual(21, result)

if __name__ == '__main__':
    unittest.main() 
