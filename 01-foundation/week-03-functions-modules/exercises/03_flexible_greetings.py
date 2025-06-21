# Exercise 3: Flexible Greeting Function
# TODO: Create a flexible greeting function with default parameters

def greet(name, greeting="Hello", punctuation="!", title=None):
    """
    Create a flexible greeting message
    
    Args:
        name (str): The person's name
        greeting (str): The greeting word (default: "Hello")
        punctuation (str): Ending punctuation (default: "!")
        title (str): Optional title (Mr., Ms., Dr., etc.)
    
    Returns:
        str: The formatted greeting message
    """
    # TODO: Implement the greeting function
    # Examples:
    # greet("Alice") -> "Hello, Alice!"
    # greet("Bob", "Hi") -> "Hi, Bob!"
    # greet("Dr. Smith", "Good morning", ".", "Dr.") -> "Good morning, Dr. Dr. Smith."
    pass

def greet_multiple(*names, greeting="Hello"):
    """
    Greet multiple people at once
    
    Args:
        *names: Variable number of names
        greeting: The greeting to use
    
    Returns:
        list: List of greeting messages
    """
    # TODO: Create greetings for all names
    pass

def custom_greet(**kwargs):
    """
    Create a custom greeting using keyword arguments
    
    Args:
        **kwargs: Keyword arguments for customization
            - name: Person's name
            - time_of_day: morning, afternoon, evening
            - formal: True/False for formal greeting
            - language: en, es, fr for different languages
    
    Returns:
        str: Customized greeting
    """
    # TODO: Create different greetings based on parameters
    # Examples:
    # custom_greet(name="Alice", time_of_day="morning") -> "Good morning, Alice!"
    # custom_greet(name="Bob", formal=True) -> "Good day, Mr. Bob!"
    # custom_greet(name="Carlos", language="es") -> "¡Hola, Carlos!"
    pass

def greeting_stats(*greetings):
    """
    Analyze greeting statistics
    
    Args:
        *greetings: Variable number of greeting strings
    
    Returns:
        dict: Statistics about the greetings
    """
    # TODO: Return statistics like:
    # - Total greetings
    # - Average length
    # - Most common words
    # - Longest greeting
    pass

# Test your functions
if __name__ == "__main__":
    print("Testing greeting functions...")
    
    # TODO: Test all your functions with different parameters
    
    # Test basic greet function
    print(greet("Alice"))
    print(greet("Bob", "Hi"))
    print(greet("Dr. Smith", "Good morning", ".", "Dr."))
    
    # Test multiple greetings
    print(greet_multiple("Alice", "Bob", "Charlie"))
    print(greet_multiple("John", "Jane", greeting="Hey"))
    
    # Test custom greetings
    print(custom_greet(name="Alice", time_of_day="morning"))
    print(custom_greet(name="Bob", formal=True))
    print(custom_greet(name="Carlos", language="es"))
    
    # Test greeting statistics
    sample_greetings = [
        "Hello, Alice!",
        "Hi, Bob!",
        "Good morning, Charlie!",
        "Hey there, David!"
    ]
    print(greeting_stats(*sample_greetings))
