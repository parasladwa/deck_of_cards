import random


#constants for creating deck
VALUES = list(range(2, 15))

SUITS = ["clubs", "diamonds", "hearts", "spades"]

FACE_VALUES = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}





#class of cards
class Card:
    
    def __init__(self, value, suit):
        self.value= value
        self.suit = suit

    
    


#iterate through values and cards, creating deck
def generate_cards(VALUES, SUITS):
    
    cards = [] 
    
    for value in VALUES:
        for suit in SUITS:
            
            #if card val has face, use dict
            if value in FACE_VALUES:
                
                card_value = FACE_VALUES[value]
                cards.append(Card(card_value, suit))
                
            else:
                cards.append(Card(value, suit))
    
    return cards




def shuffle(deck):
    
    #new deck to add cards in random order
    shuffled_deck = []
    
    while len(shuffled_deck) != 52:
        
        #select random card
        
        random_card = random.choice(deck)
        
        if random_card not in shuffled_deck:
            
            #add to new deck
            shuffled_deck.append(random_card)
            
            #remove selected card from deck
            deck.remove(random_card)
        
    return shuffled_deck
       



def main():
    
    ordered_deck = generate_cards(VALUES, SUITS)
    
    deck = shuffle(ordered_deck)

    for card in deck:
        print(card.value, card.suit)
        





























































