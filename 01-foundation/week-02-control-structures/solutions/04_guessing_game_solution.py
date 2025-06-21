# Solution 4: Number Guessing Game

import random

def play_guessing_game():
    """Main game function"""
    print("=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100!")
    
    # Game settings
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    
    print(f"You have {max_attempts} attempts to guess the number.")
    print("Enter 'quit' at any time to exit.\n")
    
    while attempts < max_attempts:
        try:
            # Get user input
            user_input = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ").strip()
            
            # Check for quit command
            if user_input.lower() == 'quit':
                print(f"Thanks for playing! The number was {secret_number}.")
                return False
            
            # Convert to integer
            guess = int(user_input)
            attempts += 1
            
            # Validate range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
            
            # Check the guess
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed it!")
                print(f"The number was {secret_number}")
                print(f"You won in {attempts} attempt(s)!")
                
                # Score calculation
                score = max(100 - (attempts - 1) * 10, 10)
                print(f"Your score: {score} points")
                
                return True
            
            elif guess < secret_number:
                difference = secret_number - guess
                if difference <= 5:
                    print(f"📈 Too low, but you're very close!")
                elif difference <= 10:
                    print(f"📈 Too low, but you're getting warm!")
                else:
                    print(f"📈 Too low! Try a higher number.")
            
            else:  # guess > secret_number
                difference = guess - secret_number
                if difference <= 5:
                    print(f"📉 Too high, but you're very close!")
                elif difference <= 10:
                    print(f"📉 Too high, but you're getting warm!")
                else:
                    print(f"📉 Too high! Try a lower number.")
            
            # Show remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempt(s) left.\n")
        
        except ValueError:
            print("Please enter a valid number!")
            continue
        except KeyboardInterrupt:
            print(f"\nGame interrupted! The number was {secret_number}.")
            return False
    
    # Game over - no more attempts
    print(f"\n😞 Game Over! You've used all {max_attempts} attempts.")
    print(f"The number was {secret_number}.")
    return False

def main():
    """Main program with play again option"""
    games_played = 0
    games_won = 0
    
    print("🎯 Welcome to the Number Guessing Game!")
    print("Try to guess the secret number between 1 and 100!")
    
    while True:
        games_played += 1
        
        # Play one game
        won = play_guessing_game()
        if won:
            games_won += 1
        
        # Show statistics
        print(f"\n📊 Your Statistics:")
        print(f"Games played: {games_played}")
        print(f"Games won: {games_won}")
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print(f"Win rate: {win_rate:.1f}%")
        
        # Play again?
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'yes']:
                print("\n" + "="*50)
                break
            elif play_again in ['n', 'no']:
                print("\nThanks for playing! Goodbye! 👋")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

# Difficulty levels (bonus feature)
def select_difficulty():
    """Allow user to select difficulty level"""
    print("\nSelect difficulty level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")  
    print("3. Hard (1-200, 5 attempts)")
    print("4. Expert (1-500, 3 attempts)")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                return 50, 10
            elif choice == 2:
                return 100, 7
            elif choice == 3:
                return 200, 5
            elif choice == 4:
                return 500, 3
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

# Start the game
if __name__ == "__main__":
    main()
