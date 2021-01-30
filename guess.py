class Guess:
    """A maneuver in the game. The responsibility of Guess is to keep track of the guesses.
    
    Stereotype: 
        Information Holder

    Attributes:
        _attempt (integer): The attempt or guess from a player
    """
    def __init__(self, attempt):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._attempt = attempt

    def get_attempt(self):
        """Returns the guess

        Args:
            self (Guess): an instance of Guess.
        """
        return self._attempt
