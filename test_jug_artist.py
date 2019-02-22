import unittest
from jug_artist import initialize_deck, get_hands, compare_cards, gameplay

class PianitzaTestCase(unittest.TestCase):
    """Tests for 'jug_artist.py'."""
    
    def setUp(self):
        """ Creates a deck, hands, and some other tested variables."""
        self.deck = initialize_deck()
        self.hands = get_hands(self.deck)
        self.all_active = list(range(4))
        self.suit_conflict = [(6,'♣'), (9,'♣'), (7,'♣'), (8,'♣')]
        self.rare_conflict = [(9,'♣'), (9,'♥'), (9,'♠'), (9,'♦')]
    
    def test_initialize_deck(self):
        """Does a deck contain 36 unique cards?"""
        self.assertTrue(len(self.deck) == len(set(self.deck)) == 36)
        
    def test_get_hands(self):
        """Does each hand consist of 9 unique cards?"""
        for hand in self.hands:
            self.assertTrue(len(hand) == len(set(hand)) == 9)
            
    def test_compare_cards(self):
        """Testing some conflict cases."""
        self.assertTrue(compare_cards(self.suit_conflict, self.all_active) == [1])
        self.assertTrue(compare_cards(self.rare_conflict, self.all_active) == self.all_active)
        
    #TODO: check that after every round sum of cards in hands are 36.
            
unittest.main()
