"""
Week 3 - Exercise 4: Random Games (Solution)
Collection of random-number-based games demonstrating functions and modules.
"""

import random
import math
from typing import List, Tuple, Optional


def number_guessing_game(min_num: int = 1, max_num: int = 100, max_attempts: int = 10) -> bool:
    """
    Play a number guessing game.
    
    Args:
        min_num (int): Minimum number in range
        max_num (int): Maximum number in range
        max_attempts (int): Maximum number of guesses allowed
        
    Returns:
        bool: True if player won, False if they lost
    """
    if min_num >= max_num:
        raise ValueError("min_num must be less than max_num")
    if max_attempts <= 0:
        raise ValueError("max_attempts must be positive")
    
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"\n🎯 Number Guessing Game!")
    print(f"I'm thinking of a number between {min_num} and {max_num}")
    print(f"You have {max_attempts} attempts to guess it!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
            elif guess < secret_number:
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"📈 Too low! {remaining} attempts remaining.")
                else:
                    print(f"📈 Too low!")
            else:
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"📉 Too high! {remaining} attempts remaining.")
                else:
                    print(f"📉 Too high!")
                    
        except ValueError:
            print("❌ Please enter a valid number!")
            # Don't count invalid input as an attempt
            attempts -= 1
    
    print(f"💔 Game over! The number was {secret_number}")
    return False


def dice_rolling_simulator(num_dice: int = 2, num_sides: int = 6, num_rolls: int = 1) -> List[List[int]]:
    """
    Simulate rolling dice and return results.
    
    Args:
        num_dice (int): Number of dice to roll
        num_sides (int): Number of sides on each die
        num_rolls (int): Number of times to roll the dice
        
    Returns:
        List[List[int]]: List of rolls, each containing the result of each die
    """
    if num_dice <= 0 or num_sides <= 0 or num_rolls <= 0:
        raise ValueError("All parameters must be positive")
    
    rolls = []
    for _ in range(num_rolls):
        single_roll = [random.randint(1, num_sides) for _ in range(num_dice)]
        rolls.append(single_roll)
    
    return rolls


def dice_game():
    """
    Play an interactive dice game with betting.
    """
    print("\n🎲 Dice Betting Game!")
    print("Rules: Roll two dice. Guess if the sum will be even or odd.")
    print("Correct guess doubles your bet, wrong guess loses it.")
    
    balance = 100
    print(f"Starting balance: ${balance}")
    
    while balance > 0:
        print(f"\nCurrent balance: ${balance}")
        
        # Get bet amount
        try:
            bet = int(input("Enter your bet amount (0 to quit): $"))
            if bet == 0:
                break
            if bet > balance:
                print("❌ You can't bet more than your balance!")
                continue
            if bet <= 0:
                print("❌ Bet must be positive!")
                continue
        except ValueError:
            print("❌ Please enter a valid amount!")
            continue
        
        # Get prediction
        prediction = input("Predict: (e)ven or (o)dd? ").lower().strip()
        if prediction not in ['e', 'even', 'o', 'odd']:
            print("❌ Please enter 'e' for even or 'o' for odd!")
            continue
        
        # Roll dice
        roll = dice_rolling_simulator(2, 6, 1)[0]
        total = sum(roll)
        is_even = total % 2 == 0
        
        print(f"🎲 You rolled: {roll[0]} and {roll[1]} (Total: {total})")
        
        # Check win/loss
        predicted_even = prediction in ['e', 'even']
        if (predicted_even and is_even) or (not predicted_even and not is_even):
            winnings = bet
            balance += winnings
            print(f"🎉 You won! +${winnings}")
        else:
            balance -= bet
            print(f"💔 You lost! -${bet}")
        
        if balance == 0:
            print("💸 You're broke! Game over!")
    
    print(f"Final balance: ${balance}")
    if balance > 100:
        print(f"🎉 You made ${balance - 100} profit!")
    elif balance < 100:
        print(f"💔 You lost ${100 - balance}")
    else:
        print("🤝 You broke even!")


def random_password_generator(length: int = 12, include_symbols: bool = True, 
                            include_numbers: bool = True, include_uppercase: bool = True) -> str:
    """
    Generate a random password with specified criteria.
    
    Args:
        length (int): Length of the password
        include_symbols (bool): Whether to include symbols
        include_numbers (bool): Whether to include numbers
        include_uppercase (bool): Whether to include uppercase letters
        
    Returns:
        str: Generated password
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Build character set
    chars = lowercase
    if include_uppercase:
        chars += uppercase
    if include_numbers:
        chars += numbers
    if include_symbols:
        chars += symbols
    
    # Ensure at least one character from each required category
    password = []
    
    # Add at least one from each category
    password.append(random.choice(lowercase))
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_symbols:
        password.append(random.choice(symbols))
    
    # Fill remaining length with random characters
    for _ in range(length - len(password)):
        password.append(random.choice(chars))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)


def lottery_simulator(num_picks: int = 6, max_number: int = 49, num_tickets: int = 1) -> dict:
    """
    Simulate a lottery drawing.
    
    Args:
        num_picks (int): Number of numbers to pick
        max_number (int): Maximum number that can be picked
        num_tickets (int): Number of tickets to generate
        
    Returns:
        dict: Results of the lottery simulation
    """
    if num_picks > max_number:
        raise ValueError("Cannot pick more numbers than available")
    if num_picks <= 0 or max_number <= 0 or num_tickets <= 0:
        raise ValueError("All parameters must be positive")
    
    # Generate winning numbers
    winning_numbers = sorted(random.sample(range(1, max_number + 1), num_picks))
    
    # Generate tickets
    tickets = []
    match_counts = {i: 0 for i in range(num_picks + 1)}
    
    for ticket_num in range(num_tickets):
        ticket = sorted(random.sample(range(1, max_number + 1), num_picks))
        matches = len(set(ticket) & set(winning_numbers))
        tickets.append({
            'ticket_number': ticket_num + 1,
            'numbers': ticket,
            'matches': matches
        })
        match_counts[matches] += 1
    
    return {
        'winning_numbers': winning_numbers,
        'tickets': tickets,
        'match_statistics': match_counts,
        'total_tickets': num_tickets
    }


def coin_flip_streak_game() -> int:
    """
    Play a coin flip streak game.
    
    Returns:
        int: Maximum streak achieved
    """
    print("\n🪙 Coin Flip Streak Game!")
    print("Keep flipping coins and try to get the longest streak!")
    print("Press Enter to flip, or type 'quit' to stop.")
    
    current_streak = 0
    max_streak = 0
    last_result = None
    total_flips = 0
    
    while True:
        user_input = input(f"\nCurrent streak: {current_streak} | Max streak: {max_streak} | Press Enter to flip: ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        # Flip coin
        result = random.choice(['Heads', 'Tails'])
        total_flips += 1
        
        print(f"🪙 Result: {result}")
        
        # Check streak
        if result == last_result:
            current_streak += 1
        else:
            current_streak = 1
        
        max_streak = max(max_streak, current_streak)
        last_result = result
    
    print(f"\n🏁 Game Summary:")
    print(f"Total flips: {total_flips}")
    print(f"Maximum streak: {max_streak}")
    
    return max_streak


def rock_paper_scissors_tournament(num_rounds: int = 5) -> dict:
    """
    Play a rock-paper-scissors tournament against the computer.
    
    Args:
        num_rounds (int): Number of rounds to play
        
    Returns:
        dict: Tournament results
    """
    if num_rounds <= 0:
        raise ValueError("Number of rounds must be positive")
    
    choices = ['rock', 'paper', 'scissors']
    player_wins = 0
    computer_wins = 0
    ties = 0
    round_results = []
    
    print(f"\n✂️ Rock Paper Scissors Tournament! (Best of {num_rounds})")
    
    for round_num in range(1, num_rounds + 1):
        print(f"\n--- Round {round_num} ---")
        
        # Get player choice
        while True:
            player_choice = input("Choose (r)ock, (p)aper, or (s)cissors: ").lower().strip()
            if player_choice in ['r', 'rock']:
                player_choice = 'rock'
                break
            elif player_choice in ['p', 'paper']:
                player_choice = 'paper'
                break
            elif player_choice in ['s', 'scissors']:
                player_choice = 'scissors'
                break
            else:
                print("❌ Invalid choice! Please enter r, p, or s.")
        
        # Computer choice
        computer_choice = random.choice(choices)
        
        print(f"You chose: {player_choice.title()}")
        print(f"Computer chose: {computer_choice.title()}")
        
        # Determine winner
        if player_choice == computer_choice:
            result = "tie"
            ties += 1
            print("🤝 It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            result = "player"
            player_wins += 1
            print("🎉 You win this round!")
        else:
            result = "computer"
            computer_wins += 1
            print("🤖 Computer wins this round!")
        
        round_results.append({
            'round': round_num,
            'player_choice': player_choice,
            'computer_choice': computer_choice,
            'result': result
        })
        
        print(f"Score: You {player_wins} - {computer_wins} Computer")
    
    # Final results
    print(f"\n🏆 Tournament Results:")
    print(f"Your wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Ties: {ties}")
    
    if player_wins > computer_wins:
        print("🎉 You won the tournament!")
        winner = "player"
    elif computer_wins > player_wins:
        print("🤖 Computer won the tournament!")
        winner = "computer"
    else:
        print("🤝 Tournament ended in a tie!")
        winner = "tie"
    
    return {
        'winner': winner,
        'player_wins': player_wins,
        'computer_wins': computer_wins,
        'ties': ties,
        'rounds': round_results
    }


def main():
    """Main function to run the random games menu."""
    print("🎮 Welcome to Random Games Collection!")
    
    while True:
        print("\n" + "="*50)
        print("🎮 RANDOM GAMES MENU")
        print("="*50)
        print("1. 🎯 Number Guessing Game")
        print("2. 🎲 Dice Betting Game")
        print("3. 🔐 Password Generator")
        print("4. 🎟️ Lottery Simulator")
        print("5. 🪙 Coin Flip Streak Game")
        print("6. ✂️ Rock Paper Scissors Tournament")
        print("7. 🚪 Exit")
        
        choice = input("\nSelect a game (1-7): ").strip()
        
        if choice == "1":
            try:
                print("\n🎯 Configure Number Guessing Game:")
                min_num = int(input("Minimum number (default 1): ") or "1")
                max_num = int(input("Maximum number (default 100): ") or "100")
                max_attempts = int(input("Maximum attempts (default 10): ") or "10")
                
                number_guessing_game(min_num, max_num, max_attempts)
            except ValueError as e:
                print(f"❌ Error: {e}")
        
        elif choice == "2":
            dice_game()
        
        elif choice == "3":
            try:
                print("\n🔐 Password Generator:")
                length = int(input("Password length (default 12): ") or "12")
                include_symbols = input("Include symbols? (y/n, default y): ").lower().strip() != 'n'
                include_numbers = input("Include numbers? (y/n, default y): ").lower().strip() != 'n'
                include_uppercase = input("Include uppercase? (y/n, default y): ").lower().strip() != 'n'
                
                password = random_password_generator(length, include_symbols, include_numbers, include_uppercase)
                print(f"\n🔐 Generated password: {password}")
                
                # Generate multiple passwords if requested
                num_passwords = int(input("Generate how many passwords? (default 1): ") or "1")
                if num_passwords > 1:
                    print(f"\n🔐 Generated {num_passwords} passwords:")
                    for i in range(num_passwords):
                        pwd = random_password_generator(length, include_symbols, include_numbers, include_uppercase)
                        print(f"{i+1:2d}. {pwd}")
                        
            except ValueError as e:
                print(f"❌ Error: {e}")
        
        elif choice == "4":
            try:
                print("\n🎟️ Lottery Simulator:")
                num_picks = int(input("Numbers to pick (default 6): ") or "6")
                max_number = int(input("Maximum number (default 49): ") or "49")
                num_tickets = int(input("Number of tickets (default 1): ") or "1")
                
                results = lottery_simulator(num_picks, max_number, num_tickets)
                
                print(f"\n🎟️ Lottery Results:")
                print(f"Winning numbers: {results['winning_numbers']}")
                
                if num_tickets <= 10:
                    print(f"\nYour tickets:")
                    for ticket in results['tickets']:
                        print(f"Ticket {ticket['ticket_number']}: {ticket['numbers']} ({ticket['matches']} matches)")
                
                print(f"\nMatch statistics:")
                for matches, count in results['match_statistics'].items():
                    if count > 0:
                        percentage = (count / num_tickets) * 100
                        print(f"{matches} matches: {count} tickets ({percentage:.1f}%)")
                        
            except ValueError as e:
                print(f"❌ Error: {e}")
        
        elif choice == "5":
            coin_flip_streak_game()
        
        elif choice == "6":
            try:
                num_rounds = int(input("Number of rounds (default 5): ") or "5")
                rock_paper_scissors_tournament(num_rounds)
            except ValueError as e:
                print(f"❌ Error: {e}")
        
        elif choice == "7":
            print("👋 Thanks for playing! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please select 1-7.")


if __name__ == "__main__":
    main()
