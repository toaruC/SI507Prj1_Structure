# Hello World!
####  This is Hanne's Project 1 for SI 507

------------

1. There is a bug in the line 24 of SI507F17_project1_cards.py, that
`return "{} of {}".format(self.rank_num,self.suit)` should be `return "{} of {}".format(self.rank,self.suit)`. It mistakes the variable ***rank_num*** for the variable ***rank***.
<br/>

2. Another bug is located in the line 55-60 of SI507F17_project1_cards.py, that

        def sort_cards(self):
            self.cards = []
            for suit in range(4):
                for rank in range(1,14):
                    card = Card(suit,rank)
                    self.cards.append(card)
        end

    returns a new deck with 52 cards in ascending sequence rather than a sorted deck based on the remaining cards in that deck.
<br/><br/>

3. Not sure if it is a bug, but as the description for "War" game goes, the dealt cards should be picked up from the tail of the deck since all cards are faced-down in the beginning. 
    In the line 64-65 of SI507F17_project1_cards.py, it picks cards from the top of the card sequence with `for i in range(hand_size): hand_cards.append(self.pop_card(i))`. I think it should be `for i in range(hand_size): hand_cards.append(self.pop_card())`.
    If there is no need to consider the sequence then I'll not count it as a bug!
<br/><br/>

4. The last bug occurs in the function show_song() in the line 110-114 of SI507F17_project1_cards.py. Even the default search term "Winner" returns results without a track title including "Winner". Meanwhile, using other search terms doesn't work at all either.
<br/>