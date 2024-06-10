# Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
# subclass the data structures to implement blackjack.
from collections import namedtuple
import random

Card = namedtuple('Card', ['ranks', 'suits'])
    
class Deck:
    ranks = [str(n) for n in range(2, 11)] + ['Jack', 'King', 'Queen', 'Ace']
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                       for suit in self.suits]
        random.shuffle(self._cards)
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    def draw(self):
        return self._cards.pop()
        
    
class BlackJackCard(Card):
    
    def getValue(self):
        if self.ranks in ['Jack', 'King', 'Queen']:
            return 10
        else:
            if self.ranks == 'Ace':
                return 11 #resole this in BlackJackHand
            else:
                return int(self.ranks)
        

class Hand:
    def __init__(self):
        self.cards = []
    
    def addCard(self, card):
        self.cards.append(card)
    
    def __str__(self):
        return ', '.join([f'{card.ranks} of {card.suits}' for card in self.cards])
        
class BlackJackHand(Hand):
    def get_score(self):
        score = 0
        aces = 0
        for card in self.cards:
            if isinstance(card, BlackJackCard):
                if card.ranks == 'Ace':
                    aces += 1
                score += card.getValue()
        
        while score > 21 and aces:
            score -= 10
            aces -= 1
        
        return score
    
    def is_blackjack(self):
        return self.get_score() == 21
    
    def is_bust(self):
        return self.get_score() > 21

if __name__ =='__main__':
    # deck = Deck()
    # print(len(deck))
    #print(deck[0])
    
    # Create a generic deck and hand
    generic_deck = Deck()
    print(f"Generic deck has {len(generic_deck)} cards")
    print(f"First card in the generic deck: {generic_deck[0]}")

    generic_hand = Hand()
    generic_hand.addCard(generic_deck.draw())
    generic_hand.addCard(generic_deck.draw())
    print(f"Generic hand cards: {generic_hand}")

    # Create a blackjack deck and hand
    blackjack_deck = Deck()
    blackjack_hand = BlackJackHand()
    blackjack_hand.addCard(BlackJackCard(*blackjack_deck.draw()))
    blackjack_hand.addCard(BlackJackCard(*blackjack_deck.draw()))
    print(f"Blackjack hand cards: {blackjack_hand}")
    print(f"Blackjack hand score: {blackjack_hand.get_score()}")
    print(f"Is blackjack? {blackjack_hand.is_blackjack()}")
    print(f"Is bust? {blackjack_hand.is_bust()}")
    #hand = Hand()