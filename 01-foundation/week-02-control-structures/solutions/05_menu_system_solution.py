# Solution 5: Interactive Menu System (Weekend Project)

import random
import math

def main_menu():
    """Display the main menu and handle user choices"""
    
    print("="*50)
    print("         INTERACTIVE MENU SYSTEM")
    print("="*50)
    
    while True:
        print("\n📋 MAIN MENU")
        print("1. 🧮 Calculator")
        print("2. 🎲 Number Games")
        print("3. 📊 Text Analyzer") 
        print("4. 🌡️  Temperature Converter")
        print("5. ℹ️  About")
        print("6. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            calculator_menu()
        elif choice == '2':
            games_menu()
        elif choice == '3':
            text_analyzer()
        elif choice == '4':
            temperature_converter()
        elif choice == '5':
            show_about()
        elif choice == '6':
            print("👋 Thank you for using the Interactive Menu System!")
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1-6.")

def calculator_menu():
    """Calculator submenu"""
    print("\n" + "="*40)
    print("           🧮 CALCULATOR")
    print("="*40)
    
    while True:
        print("\nAvailable operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Back to Main Menu")
        
        choice = input("\nSelect operation (1-7): ").strip()
        
        if choice == '7':
            break
        elif choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = num1 + num2
                    print(f"📊 {num1} + {num2} = {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"📊 {num1} - {num2} = {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"📊 {num1} × {num2} = {result}")
                elif choice == '4':
                    if num2 == 0:
                        print("❌ Error: Cannot divide by zero!")
                    else:
                        result = num1 / num2
                        print(f"📊 {num1} ÷ {num2} = {result}")
                elif choice == '5':
                    result = num1 ** num2
                    print(f"📊 {num1} ^ {num2} = {result}")
                    
            except ValueError:
                print("❌ Error: Please enter valid numbers!")
            except Exception as e:
                print(f"❌ Error: {e}")
                
        elif choice == '6':
            try:
                num = float(input("Enter number: "))
                if num < 0:
                    print("❌ Error: Cannot calculate square root of negative number!")
                else:
                    result = math.sqrt(num)
                    print(f"📊 √{num} = {result}")
            except ValueError:
                print("❌ Error: Please enter a valid number!")
        else:
            print("❌ Invalid choice!")

def games_menu():
    """Games submenu"""
    print("\n" + "="*40)
    print("           🎲 NUMBER GAMES")
    print("="*40)
    
    while True:
        print("\nAvailable games:")
        print("1. 🔢 Number Guessing Game")
        print("2. ✂️  Rock, Paper, Scissors")
        print("3. 🧠 Math Quiz")
        print("4. 🎯 Lucky Number Generator")
        print("5. Back to Main Menu")
        
        choice = input("\nSelect game (1-5): ").strip()
        
        if choice == '5':
            break
        elif choice == '1':
            number_guessing_game()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            math_quiz()
        elif choice == '4':
            lucky_number_generator()
        else:
            print("❌ Invalid choice!")

def number_guessing_game():
    """Simple number guessing game"""
    print("\n🔢 Number Guessing Game")
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"Guess the number between 1 and 100! You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
            attempts += 1
            
            if guess == secret:
                print(f"🎉 Correct! You won in {attempts} attempts!")
                return
            elif guess < secret:
                print("📈 Too low!")
            else:
                print("📉 Too high!")
                
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"😞 Game over! The number was {secret}")

def rock_paper_scissors():
    """Rock, Paper, Scissors game"""
    print("\n✂️ Rock, Paper, Scissors")
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    rounds = 0
    
    while True:
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        user_choice = input("Enter rock, paper, scissors (or 'quit'): ").lower().strip()
        
        if user_choice == 'quit':
            break
        elif user_choice not in choices:
            print("Invalid choice!")
            continue
            
        computer_choice = random.choice(choices)
        rounds += 1
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😞 Computer wins this round!")
            computer_score += 1
    
    if rounds > 0:
        print(f"\nFinal Score after {rounds} rounds:")
        print(f"You: {user_score}, Computer: {computer_score}")
        if user_score > computer_score:
            print("🏆 You won overall!")
        elif computer_score > user_score:
            print("🤖 Computer won overall!")
        else:
            print("🤝 Overall tie!")

def math_quiz():
    """Simple math quiz"""
    print("\n🧠 Math Quiz")
    score = 0
    questions = 5
    
    for i in range(questions):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
        
        if operation == '+':
            answer = num1 + num2
        elif operation == '-':
            answer = num1 - num2
        else:  # multiplication
            answer = num1 * num2
        
        try:
            user_answer = int(input(f"Question {i+1}: {num1} {operation} {num2} = "))
            if user_answer == answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The answer was {answer}")
        except ValueError:
            print(f"❌ Invalid input! The answer was {answer}")
    
    print(f"\nQuiz completed! Your score: {score}/{questions}")
    percentage = (score / questions) * 100
    print(f"Percentage: {percentage:.1f}%")

def lucky_number_generator():
    """Generate lucky numbers"""
    print("\n🎯 Lucky Number Generator")
    
    try:
        count = int(input("How many lucky numbers do you want? "))
        min_num = int(input("Minimum number: "))
        max_num = int(input("Maximum number: "))
        
        if min_num >= max_num:
            print("❌ Minimum must be less than maximum!")
            return
        
        print(f"\n🍀 Your {count} lucky numbers:")
        lucky_numbers = []
        for i in range(count):
            num = random.randint(min_num, max_num)
            lucky_numbers.append(num)
        
        for i, num in enumerate(lucky_numbers, 1):
            print(f"{i}. {num}")
        
        # Some fun analysis
        if len(lucky_numbers) > 1:
            print(f"\n📊 Analysis:")
            print(f"Sum: {sum(lucky_numbers)}")
            print(f"Average: {sum(lucky_numbers)/len(lucky_numbers):.2f}")
            print(f"Highest: {max(lucky_numbers)}")
            print(f"Lowest: {min(lucky_numbers)}")
            
    except ValueError:
        print("❌ Please enter valid numbers!")

def text_analyzer():
    """Text analysis tool"""
    print("\n" + "="*40)
    print("           📊 TEXT ANALYZER")
    print("="*40)
    
    text = input("\nEnter text to analyze: ").strip()
    
    if not text:
        print("❌ No text entered!")
        return
    
    # Basic counts
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Vowels and consonants
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    
    # Find longest word
    words = text.split()
    if words:
        longest_word = max(words, key=len)
        shortest_word = min(words, key=len)
    else:
        longest_word = "None"
        shortest_word = "None"
    
    # Display results
    print(f"\n📊 ANALYSIS RESULTS")
    print(f"{'='*30}")
    print(f"Total characters: {char_count}")
    print(f"Characters (no spaces): {char_count_no_spaces}")
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Longest word: '{longest_word}' ({len(longest_word)} chars)")
    print(f"Shortest word: '{shortest_word}' ({len(shortest_word)} chars)")
    
    # Additional analysis
    if word_count > 0:
        avg_word_length = char_count_no_spaces / word_count
        print(f"Average word length: {avg_word_length:.2f} characters")
    
    # Word frequency (top 3)
    word_freq = {}
    for word in text.lower().split():
        word_clean = ''.join(char for char in word if char.isalnum())
        if word_clean:
            word_freq[word_clean] = word_freq.get(word_clean, 0) + 1
    
    if word_freq:
        top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]
        print(f"\nMost frequent words:")
        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i}. '{word}' - {count} time(s)")

def temperature_converter():
    """Temperature conversion tool"""
    print("\n" + "="*40)
    print("         🌡️ TEMPERATURE CONVERTER")
    print("="*40)
    
    print("\nConversion options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    try:
        choice = input("\nSelect conversion (1-6): ").strip()
        temp = float(input("Enter temperature: "))
        
        if choice == '1':
            result = (temp * 9/5) + 32
            print(f"🌡️ {temp}°C = {result:.2f}°F")
        elif choice == '2':
            result = (temp - 32) * 5/9
            print(f"🌡️ {temp}°F = {result:.2f}°C")
        elif choice == '3':
            result = temp + 273.15
            print(f"🌡️ {temp}°C = {result:.2f}K")
        elif choice == '4':
            if temp < 0:
                print("❌ Kelvin cannot be negative!")
                return
            result = temp - 273.15
            print(f"🌡️ {temp}K = {result:.2f}°C")
        elif choice == '5':
            result = (temp - 32) * 5/9 + 273.15
            print(f"🌡️ {temp}°F = {result:.2f}K")
        elif choice == '6':
            if temp < 0:
                print("❌ Kelvin cannot be negative!")
                return
            result = (temp - 273.15) * 9/5 + 32
            print(f"🌡️ {temp}K = {result:.2f}°F")
        else:
            print("❌ Invalid choice!")
            return
        
        # Temperature insights
        if choice in ['1', '2']:  # Celsius/Fahrenheit conversions
            if choice == '1':  # C to F
                celsius = temp
                fahrenheit = result
            else:  # F to C
                celsius = result
                fahrenheit = temp
            
            if celsius <= 0:
                print("🧊 Freezing point of water or below!")
            elif celsius >= 100:
                print("💨 Boiling point of water or above!")
            elif celsius >= 37:
                print("🔥 Human body temperature or above!")
            elif celsius >= 20 and celsius <= 25:
                print("🌡️ Comfortable room temperature!")
                
    except ValueError:
        print("❌ Please enter a valid number!")

def show_about():
    """Show information about the program"""
    print("\n" + "="*50)
    print("                    ℹ️ ABOUT")
    print("="*50)
    print("""
📋 Interactive Menu System v1.0

This program demonstrates fundamental Python programming concepts:
• Conditional statements (if/elif/else)
• Loops (for/while)
• User input handling
• Error handling with try/except
• Function organization
• Menu-driven programming

🎯 Features:
• Calculator with basic operations
• Fun number games
• Text analysis tools
• Temperature conversion
• Interactive user interface

👨‍💻 Created as part of Python Learning Week 2
🎓 Focus: Control Structures and Program Flow

💡 This project showcases:
✓ Menu navigation
✓ Input validation
✓ Error handling
✓ Code organization
✓ User experience design

🚀 Perfect for beginners learning Python control structures!
    """)
    
    input("\nPress Enter to continue...")

# Start the program
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please restart the program.")
