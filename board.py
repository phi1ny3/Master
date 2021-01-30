import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): The number of piles of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._attempt = []
        self._prepare()

    def encode(correct, guess):

        output_arr = [''] * len(correct)
 
        for i, (correct_num, guess_num) in enumerate(self._correct, guess)):
            output_arr[i] = 'X' if guess_num == correct_num else 'O' if guess_num in correct else '-'
 
            return ''.join(output_arr)

    def _prepare(self):
        """Sets up the board with the numbers randomly generated
        
        Args:
            self (Board): an instance of Board.
        """
        number_of_numbers = 10
        code_length = safe_int_input("How long is the code to be guessed? (4-10): ", 4, 10)
        numbers = '1234567890'[:number_of_numbers]
        code = ''.join(random.choices(numbers, k=code_length))
    guesses = []