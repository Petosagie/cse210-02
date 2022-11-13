import random

class Cards:
    '''A stack of cards labeled 1-13.
    The responsibilty of Cards is to keep track of the card that is generated, and apply the points associated with it.
    
    Attributes:
    number (int): The number of the chosen card
    points (int): The number of points the correct or incorrect choice is worth
    choice (str): The user input that is h or l
    '''

    def __init__(self):
        '''Constructs a new instance of Cards with a number and points attribute.
        Args:
        self (Cards): An instance of Cards.
        '''
        self.current_card_num = random.randint(1, 13)
        self.next_card_num = random.randint(1, 13)

    def select_card(self, choice):
        '''Generates a new random card and calculates the points
        
        Args:
        self (Cards): An instance of Cards
        choice: the user's input
        '''
        
        points = 0

        if choice == 'h' and self.next_card_num > self.current_card_num:
            points +=  100

        if choice == 'l' and self.next_card_num < self.current_card_num:
            points += 100

        if choice == 'h' and self.next_card_num < self.current_card_num:
            points -= 75

        if choice == 'l' and self.next_card_num > self.current_card_num:
            points -= 75
    
        self.current_card_num = self.next_card_num
        self.next_card_num = random.randint(1, 13)
            
        return points