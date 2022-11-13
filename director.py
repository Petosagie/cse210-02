from cards import Cards
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        cards (List[Cards]): A list of card instances.
        total_points (int): The score for the entire game.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = Cards()
        self.is_playing = True
        self.total_points = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.higher_or_lower()
            self.do_outputs()
            self.game_restart()

    def higher_or_lower(self):
        '''Ask the user if the next card is higher or lower and updates their score
        Args:
        self(Director): An instance of Director
        ''' 
        if not self.is_playing:
            return
        print('              ___')
        print(f'The card is  | {self.cards.current_card_num} |')
        print('             |___|')
        while True:       
            h_or_l = input('Higher or Lower [h/l]: ')
            if (h_or_l.lower() == "h") or (h_or_l.lower() == "l"):
                print(h_or_l)
                break
            print(f"Sorry, {h_or_l} was not recognized.")
        
        self.total_points += self.cards.select_card(h_or_l)

    def do_outputs(self):
        """Displays the card chosen and the score. Also asks the player if they want to choose another card. 
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print('                    ___')
        print(f'The next card was: | {self.cards.current_card_num} |')
        print('                   |___|')
        print(f"Your score is: {self.total_points}\n")
        self.is_playing == (self.total_points > 0)
        
        
    def game_restart(self):
        while True:
            y_n = input('Play again? [y/n]: ')
            if (y_n.lower() == "y") or (y_n.lower() == "n"):
                if self.total_points > 0:
                    self.is_playing = (y_n == "y")
                elif self.total_points <= 0:
                    print("Sorry! you are out of points.")
                    self.is_playing = False
                break
            print(f"Sorry, {y_n} was not recognized.")