# Exercise 5: Interactive Menu System (Weekend Project)
# TODO: Create a comprehensive menu system with multiple options

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
        
        # TODO: Implement menu handling using if/elif statements
        # Call appropriate functions based on user choice
        
        # Your code here:

def calculator_menu():
    """Calculator submenu"""
    # TODO: Create a calculator with basic operations
    # - Addition, subtraction, multiplication, division
    # - Handle division by zero
    # - Allow multiple calculations
    pass

def games_menu():
    """Games submenu"""
    # TODO: Create a games menu with options:
    # - Number guessing game
    # - Rock, Paper, Scissors
    # - Simple math quiz
    pass

def text_analyzer():
    """Text analysis tool"""
    # TODO: Analyze text input:
    # - Count characters, words, sentences
    # - Find longest word
    # - Count vowels and consonants
    pass

def temperature_converter():
    """Temperature conversion tool"""
    # TODO: Convert between Celsius, Fahrenheit, and Kelvin
    # - Provide conversion formulas
    # - Handle invalid input
    pass

def show_about():
    """Show information about the program"""
    # TODO: Display program information
    pass

# Start the program
if __name__ == "__main__":
    main_menu()
