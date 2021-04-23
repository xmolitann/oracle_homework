import unittest
import deck_of_cards.deck_of_cards as doc


class TestDeck(unittest.TestCase):
    def testInit(self):
        deck = doc.Deck()
        self.assertEqual(52, len(deck.cards))

    def testShuffle(self):
        deck_before = doc.Deck()
        deck_after = deck_before.shuffle()
        self.assertNotEqual(deck_after, deck_before)

    def testDeal(self):
        deck = doc.Deck()
        last_card = deck.cards[-1]
        dealt_card = deck.deal()
        self.assertEqual(last_card, dealt_card)

    def testRemaining(self):
        deck = doc.Deck()
        self.assertEqual(52, doc.Deck.remaining(deck))
        deck.deal()
        self.assertEqual(51, doc.Deck.remaining(deck))


class TestCard(unittest.TestCase):
    def testInit(self):
        card1 = {"Clubs", 3}
        card2 = {"Clubs", 3}
        self.assertEqual(card1, card2)

    def testSuit(self):
        card = doc.Card("Clubs", 3)
        self.assertEqual("Clubs", doc.Card.suit(card))

    def testValue(self):
        card = doc.Card("Clubs", 3)
        self.assertEqual(3, doc.Card.value(card))

    def testSuitAsString(self):
        deck = doc.Deck()
        card_clubs = deck.cards[0]
        card_diamonds = deck.cards[13]
        card_hearts = deck.cards[26]
        card_spades = deck.cards[39]
        self.assertEqual("Clubs", doc.Card.suitAsString(card_clubs))
        self.assertEqual("Diamonds", doc.Card.suitAsString(card_diamonds))
        self.assertEqual("Hearts", doc.Card.suitAsString(card_hearts))
        self.assertEqual("Spades", doc.Card.suitAsString(card_spades))

    def testValueAsString(self):
        deck = doc.Deck()
        card_ace = deck.cards[0]
        card_jack = deck.cards[10]
        card_queen = deck.cards[11]
        card_king = deck.cards[12]
        self.assertEqual("Ace", doc.Card.valueAsString(card_ace))
        self.assertEqual("Jack", doc.Card.valueAsString(card_jack))
        self.assertEqual("Queen", doc.Card.valueAsString(card_queen))
        self.assertEqual("King", doc.Card.valueAsString(card_king))

    def testToString(self):
        deck = doc.Deck()
        card_ace_clubs = deck.cards[0]
        card_jack_diamonds = deck.cards[23]
        card_ten_hearts = deck.cards[35]
        card_three_spades = deck.cards[41]
        self.assertEqual("Ace of Clubs", doc.Card.toString(card_ace_clubs))
        self.assertEqual("Jack of Diamonds", doc.Card.toString(card_jack_diamonds))
        self.assertEqual("10 of Hearts", doc.Card.toString(card_ten_hearts))
        self.assertEqual("3 of Spades", doc.Card.toString(card_three_spades))


class TestHand(unittest.TestCase):
    def testInit(self):
        hand = []
        init_hand = doc.Hand()
        self.assertCountEqual(hand, init_hand.hand)

    def testAddCard(self):
        hand = [{"Clubs", 3}, {"Hearts", 1}]
        init_hand = doc.Hand()
        init_hand.addCard({"Clubs", 3})
        init_hand.addCard({"Hearts", 1})
        self.assertCountEqual(hand, init_hand.hand)

    def testRemoveCard(self):
        hand = [{"Clubs", 3}]
        init_hand = doc.Hand()
        init_hand.addCard({"Clubs", 3})
        init_hand.addCard({"Hearts", 1})
        init_hand.removeCard({"Hearts", 1})
        self.assertCountEqual(hand, init_hand.hand)

    def testSortyBySuit(self):
        hand = [{"Hearts", 1}, {"Clubs", 3}, {"Spades", 6}, {"Diamonds", 11}]
        hand.sort()
        init_hand = doc.Hand()
        init_hand.addCard({"Clubs", 3})
        init_hand.addCard({"Hearts", 1})
        init_hand.addCard({"Diamonds", 11})
        init_hand.addCard({"Spades", 6})
        init_hand.sortBySuit()
        self.assertEqual(hand, init_hand.hand)

    def testSortyByValue(self):
        hand = [{"Clubs", 2}, {"Spades", 5}, {"Hearts", 11},  {"Hearts", 11}]
        init_hand = doc.Hand()
        init_hand.addCard({"Hearts", 11})
        init_hand.addCard({"Clubs", 2})
        init_hand.addCard({"Hearts", 11})
        init_hand.addCard({"Spades", 5})
        init_hand.sortByValue()
        self.assertEqual(hand, init_hand)


if __name__ == '__main__':
    unittest.main()
