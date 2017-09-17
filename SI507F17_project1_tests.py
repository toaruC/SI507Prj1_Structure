## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

import unittest
import SI507F17_project1_cards


class TestCard(unittest.TestCase):

    def test_card_default_value(self):
        default_card = Card()
        self.assertEqual(str(default_card),"2 of Diamonds","The card default value is wrong, should be 2 of Diamonds.")


    def test_card_suit_names(self):
        #test for Diamonds
        result = Card(0,3)
        self.assertEqual(result.suit, "Diamonds", "The suit name is wrong, should be Diamonds.")

        #test for Clubs
        result = Card(1,3)
        self.assertEqual(result.suit, "Clubs", "The suit name is wrong, should be Clubs.")

        #test for Hearts
        result = Card(2,3)
        self.assertEqual(result.suit, "Hearts", "The suit name is wrong, should be Hearts.")

        #test for Spades
        result = Card(3,3)
        self.assertEqual(result.suit, "Spades", "The suit name is wrong, should be Spades.")


    def test_card_faces(self):
        #test for Ace
        result = Card(0, 1)
        self.assertEqual(str(result), "Ace of Diamonds", "The suit name for faces is wrong, should be Ace.")

        #test for Jack
        result = Card(0, 11)
        self.assertEqual(str(result), "Jack of Diamonds", "The suit name for faces is wrong, should be Jack.")

        # test for Queen
        result = Card(0, 12)
        self.assertEqual(str(result), "Queen of Diamonds", "The suit name for faces is wrong, should be Queen.")

        # test for King
        result = Card(0, 13)
        self.assertEqual(str(result), "King of Diamonds", "The suit name for faces is wrong, should be King.")



class TestDesk(unittest.TestCase):

    def test_deck_default_cards_in_deck(self):

        default_cards = Deck().cards

        #test for card number
        self.assertEqual(len(default_cards), 52, "The default card number is wrong, should be 52 cards.")

        #test for the 14th card in the cards list
        self.assertEqual(str(default_cards[13]), str(Card(1,1)), "The default card sequence is wrong.")

        #test for the 52th card in the cards list
        self.assertEqual(str(default_cards[51]), str(Card(3,13)), "The default card sequence is wrong.")


    def test_deck_pop_card(self):

        dtest = Deck()
        result_a = dtest.pop_card()
        result_b = dtest.pop_card()
        result_c = dtest.pop_card(0)
        result_d = dtest.pop_card(2)

        #test for default pop
        self.assertEqual(str(result_a),str(Card(3,13)), "The default popped out card is wrong, should be King of Spades." )
        self.assertEqual(str(result_b), str(Card(3, 12)), "The default popped out card is wrong, should be Queen of Spades.")

        #test for pop with an input
        self.assertEqual(str(result_c),str(Card(0,1)), "The popped out card is wrong, should be Ace of Diamonds.")
        self.assertEqual(str(result_d), str(Card(0, 4)), "The popped out card is wrong, should be 4 of Diamonds.")


    def test_deck_shuffle(self):

        result = Deck().shuffle()
        dtest = Deck()

        self.assertTrue(str(result) != str(dtest), "The deck has not been shuffled.")


    def test_deck_replace_card(self):

        dtest = Deck()
        dtest.pop_card()

        #test for replacing an existing card in the deck -- "Ace of Diamonds"
        dtest.replace_card(Card(0,1))
        result = dtest.pop_card()
        self.assertTrue(str(result) != str(Card(0,1)), "The replaced card is duplicate in the deck.")

        #test for replacing absent cards in the deck -- "King of Spades" & "Queen of Spades"
        dtest.replace_card(Card(3,13))
        dtest.replace_card(Card(3,12))
        result_a = dtest.cards[50]
        result_b = dtest.cards[51]
        self.assertEqual(str(result_a), str(Card(3,13)), "The replaced card King of Spades is absent in the deck, should be added to the deck.")
        self.assertEqual(str(result_b), str(Card(3,12)),"The replaced card Queen of Spades is absent in the deck, should be added to the deck.")


    def test_deck_sort_cards(self):

        result = Deck()
        result.pop_card() #remove the last card
        result.pop_card(0) #remove the first card
        result.shuffle()
        result.sort_cards() #sort remaining cards

        dtest = Deck()
        dtest.pop_card()
        dtest.pop_card(0)

        self.assertEqual(len(result.cards), len(dtest.cards), "The total cards number of the sorted deck is wrong.")

        self.assertEqual(str(result), str(dtest), "The sorted result is wrong.")


    def test_deck_deal_hand(self):

        #test for 1 dealt
        result = Deck().deal_hand(1)[0]
        dtest = Deck().pop_card()
        self.assertEqual(str(result), str(dtest), "The result for one dealt in hand is wrong, should be King of Spades.")

        #test for 2 dealt
        result = Deck().deal_hand(2)
        result_list = []
        for dealt in result:
            result_list.append(str(result[dealt]))
        dtest = Deck()
        dtest_list = []
        for i in range(2):
            dtest_list.append(str(dtest.pop_card()))
        self.assertEqual(result_list, dtest_list, "The result for two dealt in hand is wrong, should be King of Spades - Queen of Spades.")


class TestFuncPlayWarGame(unittest.TestCase):

    def test_play_war_game_result(self):

        result_list = play_war_game(True)

        #test for games whose winner is Player1
        if result_list[0] == "Player1":
            self.assertTrue(result_list[1] > result_list[2], "The game result is wrong, winner should be Player2.")

        #test for games whose winner is Player2
        if result_list[0] == "Player2":
            self.assertTrue(result_list[1] < result_list[2], "The game result is wrong, winner should be Player1.")

        #test for Tie games
        if result_list[0] == "Tie":
            self.assertTrue(result_list[1] == result_list[2], "The game result is not tie.")

class TestFuncShowSong(unittest.TestCase):

    def test_show_song_default_keword(self):
        result = show_song().track
        self.assertTrue("Winner".lower() in result.lower(), "The search term Winner is not included in the result.")

    def test_show_song_other_keyword(self):
        result = show_song("Tie").track
        self.assertTrue("Tie".lower() in result.lower(), "The search term Tie is not included in the result.")

if __name__ == '__main__':
    unittest.main(verbosity=2)