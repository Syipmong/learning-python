# Exercise 4: Random Number Games with Modules
# TODO: Create games using the random module

import random
import math

def guess_my_number(min_num=1, max_num=100, max_attempts=7):
    """
    Number guessing game
    
    Args:
        min_num: Minimum number in range
        max_num: Maximum number in range  
        max_attempts: Maximum attempts allowed
    
    Returns:
        bool: True if player won, False otherwise
    """
    # TODO: Implement the guessing game using random.randint()
    pass

def dice_simulator(num_dice=2, num_sides=6, num_rolls=10):
    """
    Simulate rolling dice
    
    Args:
        num_dice: Number of dice to roll
        num_sides: Number of sides on each die
        num_rolls: Number of times to roll
    
    Returns:
        list: List of roll results
    """
    # TODO: Simulate dice rolls using random.randint()
    pass

def random_password_generator(length=12, include_numbers=True, include_symbols=True):
    """
    Generate a random password
    
    Args:
        length: Length of password
        include_numbers: Include numbers (0-9)
        include_symbols: Include symbols (!@#$%^&*)
    
    Returns:
        str: Random password
    """
    # TODO: Generate password using random.choice()
    pass

def coin_flip_experiment(num_flips=100):
    """
    Simulate coin flips and analyze results
    
    Args:
        num_flips: Number of coin flips
    
    Returns:
        dict: Results with heads/tails count and percentages
    """
    # TODO: Use random.choice() to simulate coin flips
    pass

def lottery_number_generator(num_count=6, min_num=1, max_num=49):
    """
    Generate lottery numbers
    
    Args:
        num_count: How many numbers to generate
        min_num: Minimum number
        max_num: Maximum number
    
    Returns:
        list: Sorted list of unique lottery numbers
    """
    # TODO: Use random.sample() to generate unique numbers
    pass

def random_quote_generator():
    """
    Return a random inspirational quote
    
    Returns:
        str: Random quote
    """
    # TODO: Create a list of quotes and return a random one
    quotes = [
        # Add your favorite quotes here
    ]
    pass

def calculate_probability(success_count, total_attempts):
    """
    Calculate probability percentage
    
    Args:
        success_count: Number of successful outcomes
        total_attempts: Total number of attempts
    
    Returns:
        float: Probability as percentage
    """
    # TODO: Calculate and return probability percentage
    pass

# Test your functions
if __name__ == "__main__":
    print("Testing random number games...")
    
    # TODO: Test all your functions
    
    # Test guessing game
    print("Starting guessing game...")
    # guess_my_number()
    
    # Test dice simulator
    print("\nDice simulation:")
    rolls = dice_simulator(2, 6, 5)
    print(f"Dice rolls: {rolls}")
    
    # Test password generator
    print(f"\nRandom password: {random_password_generator()}")
    
    # Test coin flip experiment
    print("\nCoin flip experiment:")
    results = coin_flip_experiment(50)
    print(results)
    
    # Test lottery numbers
    print(f"\nLottery numbers: {lottery_number_generator()}")
    
    # Test random quote
    print(f"\nRandom quote: {random_quote_generator()}")
