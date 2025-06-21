"""
Week 3 - Exercise 3: Flexible Greetings (Solution)
Dynamic greeting system with customization options and validation.
"""

import random
from datetime import datetime


def get_time_of_day():
    """
    Get the current time of day category based on the hour.
    
    Returns:
        str: Time category ('morning', 'afternoon', 'evening', 'night')
    """
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 17:
        return "afternoon"
    elif 17 <= current_hour < 21:
        return "evening"
    else:
        return "night"


def create_greeting(name, language="english", formal=True, include_time=True):
    """
    Create a personalized greeting message.
    
    Args:
        name (str): The person's name
        language (str): Language for greeting ('english', 'spanish', 'french', 'german')
        formal (bool): Whether to use formal or casual greeting
        include_time (bool): Whether to include time-based greeting
        
    Returns:
        str: The formatted greeting message
        
    Raises:
        ValueError: If name is empty or language is not supported
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    
    name = name.strip().title()
    
    # Define greetings for different languages
    greetings = {
        "english": {
            "formal": {
                "morning": f"Good morning, {name}. I hope you have a wonderful day ahead.",
                "afternoon": f"Good afternoon, {name}. I trust your day is going well.",
                "evening": f"Good evening, {name}. I hope you've had a productive day.",
                "night": f"Good evening, {name}. I hope you have a restful night.",
                "general": f"Hello, {name}. It's a pleasure to meet you."
            },
            "casual": {
                "morning": f"Hey {name}! Hope you're ready to rock this morning!",
                "afternoon": f"Hi {name}! How's your afternoon treating you?",
                "evening": f"Hey there, {name}! How was your day?",
                "night": f"Hi {name}! Hope you're winding down nicely.",
                "general": f"Hey {name}! Great to see you!"
            }
        },
        "spanish": {
            "formal": {
                "morning": f"Buenos días, {name}. Que tenga un día maravilloso.",
                "afternoon": f"Buenas tardes, {name}. Espero que su día vaya bien.",
                "evening": f"Buenas noches, {name}. Espero que haya tenido un día productivo.",
                "night": f"Buenas noches, {name}. Que tenga una noche de descanso.",
                "general": f"Hola, {name}. Es un placer conocerle."
            },
            "casual": {
                "morning": f"¡Hola {name}! ¡Espero que estés listo para esta mañana!",
                "afternoon": f"¡Hola {name}! ¿Cómo va tu tarde?",
                "evening": f"¡Hola {name}! ¿Cómo estuvo tu día?",
                "night": f"¡Hola {name}! Espero que te estés relajando.",
                "general": f"¡Hola {name}! ¡Qué bueno verte!"
            }
        },
        "french": {
            "formal": {
                "morning": f"Bonjour, {name}. J'espère que vous passerez une merveilleuse journée.",
                "afternoon": f"Bon après-midi, {name}. J'espère que votre journée se passe bien.",
                "evening": f"Bonsoir, {name}. J'espère que vous avez passé une journée productive.",
                "night": f"Bonsoir, {name}. J'espère que vous passerez une nuit reposante.",
                "general": f"Bonjour, {name}. C'est un plaisir de vous rencontrer."
            },
            "casual": {
                "morning": f"Salut {name}! J'espère que tu es prêt pour cette matinée!",
                "afternoon": f"Salut {name}! Comment se passe ton après-midi?",
                "evening": f"Salut {name}! Comment s'est passée ta journée?",
                "night": f"Salut {name}! J'espère que tu te détends bien.",
                "general": f"Salut {name}! Ravi de te voir!"
            }
        },
        "german": {
            "formal": {
                "morning": f"Guten Morgen, {name}. Ich hoffe, Sie haben einen wundervollen Tag.",
                "afternoon": f"Guten Tag, {name}. Ich hoffe, Ihr Tag verläuft gut.",
                "evening": f"Guten Abend, {name}. Ich hoffe, Sie hatten einen produktiven Tag.",
                "night": f"Guten Abend, {name}. Ich hoffe, Sie haben eine erholsame Nacht.",
                "general": f"Hallo, {name}. Es ist mir eine Freude, Sie kennenzulernen."
            },
            "casual": {
                "morning": f"Hallo {name}! Ich hoffe, du bist bereit für diesen Morgen!",
                "afternoon": f"Hi {name}! Wie läuft dein Nachmittag?",
                "evening": f"Hallo {name}! Wie war dein Tag?",
                "night": f"Hi {name}! Ich hoffe, du entspannst dich schön.",
                "general": f"Hallo {name}! Schön dich zu sehen!"
            }
        }
    }
    
    language = language.lower()
    if language not in greetings:
        raise ValueError(f"Language '{language}' not supported. Available: {list(greetings.keys())}")
    
    style = "formal" if formal else "casual"
    time_category = get_time_of_day() if include_time else "general"
    
    return greetings[language][style][time_category]


def create_farewell(name, language="english", formal=True):
    """
    Create a personalized farewell message.
    
    Args:
        name (str): The person's name
        language (str): Language for farewell
        formal (bool): Whether to use formal or casual farewell
        
    Returns:
        str: The formatted farewell message
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    
    name = name.strip().title()
    
    farewells = {
        "english": {
            "formal": [
                f"Goodbye, {name}. It was a pleasure speaking with you.",
                f"Farewell, {name}. Have a wonderful day ahead.",
                f"Take care, {name}. Until we meet again."
            ],
            "casual": [
                f"See you later, {name}!",
                f"Catch you later, {name}!",
                f"Take it easy, {name}!",
                f"Later, {name}!"
            ]
        },
        "spanish": {
            "formal": [
                f"Adiós, {name}. Fue un placer hablar con usted.",
                f"Hasta luego, {name}. Que tenga un día maravilloso.",
                f"Cuídese, {name}. Hasta que nos volvamos a ver."
            ],
            "casual": [
                f"¡Nos vemos, {name}!",
                f"¡Hasta luego, {name}!",
                f"¡Cuídate, {name}!",
                f"¡Chao, {name}!"
            ]
        },
        "french": {
            "formal": [
                f"Au revoir, {name}. Ce fut un plaisir de vous parler.",
                f"À bientôt, {name}. Passez une merveilleuse journée.",
                f"Prenez soin de vous, {name}. À la prochaine fois."
            ],
            "casual": [
                f"À plus, {name}!",
                f"Salut, {name}!",
                f"À bientôt, {name}!",
                f"Ciao, {name}!"
            ]
        },
        "german": {
            "formal": [
                f"Auf Wiedersehen, {name}. Es war mir eine Freude, mit Ihnen zu sprechen.",
                f"Bis bald, {name}. Haben Sie einen wundervollen Tag.",
                f"Passen Sie auf sich auf, {name}. Bis wir uns wiedersehen."
            ],
            "casual": [
                f"Bis später, {name}!",
                f"Tschüss, {name}!",
                f"Mach's gut, {name}!",
                f"Ciao, {name}!"
            ]
        }
    }
    
    language = language.lower()
    if language not in farewells:
        raise ValueError(f"Language '{language}' not supported. Available: {list(farewells.keys())}")
    
    style = "formal" if formal else "casual"
    return random.choice(farewells[language][style])


def conversation_flow(name, language="english"):
    """
    Create a complete conversation flow with greetings and farewells.
    
    Args:
        name (str): The person's name
        language (str): Language for the conversation
        
    Returns:
        dict: Dictionary containing greeting, conversation, and farewell
    """
    try:
        # Create both formal and casual greetings
        formal_greeting = create_greeting(name, language, formal=True, include_time=True)
        casual_greeting = create_greeting(name, language, formal=False, include_time=True)
        
        # Create farewell
        farewell = create_farewell(name, language, formal=True)
        
        return {
            "formal_greeting": formal_greeting,
            "casual_greeting": casual_greeting,
            "farewell": farewell,
            "language": language.title(),
            "name": name.title(),
            "time_of_day": get_time_of_day().title()
        }
    except ValueError as e:
        return {"error": str(e)}


def batch_greetings(names, language="english", formal=True):
    """
    Create greetings for multiple people.
    
    Args:
        names (list): List of names
        language (str): Language for greetings
        formal (bool): Whether to use formal greetings
        
    Returns:
        dict: Dictionary mapping names to their greetings
    """
    greetings = {}
    errors = {}
    
    for name in names:
        try:
            greeting = create_greeting(name, language, formal, include_time=False)
            greetings[name] = greeting
        except ValueError as e:
            errors[name] = str(e)
    
    result = {"greetings": greetings}
    if errors:
        result["errors"] = errors
    
    return result


def main():
    """Main function to demonstrate the greeting system."""
    print("=== Flexible Greeting System ===\n")
    
    while True:
        print("\nOptions:")
        print("1. Single greeting")
        print("2. Conversation flow")
        print("3. Batch greetings")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            name = input("Enter name: ")
            print("\nAvailable languages: english, spanish, french, german")
            language = input("Select language (default: english): ").strip() or "english"
            
            print("Select style:")
            print("1. Formal")
            print("2. Casual")
            style_choice = input("Enter choice (1-2): ").strip()
            formal = style_choice != "2"
            
            include_time = input("Include time-based greeting? (y/n): ").strip().lower() == "y"
            
            try:
                greeting = create_greeting(name, language, formal, include_time)
                print(f"\nGreeting: {greeting}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            name = input("Enter name: ")
            print("\nAvailable languages: english, spanish, french, german")
            language = input("Select language (default: english): ").strip() or "english"
            
            conversation = conversation_flow(name, language)
            
            if "error" in conversation:
                print(f"Error: {conversation['error']}")
            else:
                print(f"\n=== Conversation with {conversation['name']} ===")
                print(f"Language: {conversation['language']}")
                print(f"Time of day: {conversation['time_of_day']}")
                print(f"\nFormal greeting: {conversation['formal_greeting']}")
                print(f"Casual greeting: {conversation['casual_greeting']}")
                print(f"Farewell: {conversation['farewell']}")
        
        elif choice == "3":
            names_input = input("Enter names separated by commas: ")
            names = [name.strip() for name in names_input.split(",")]
            
            print("\nAvailable languages: english, spanish, french, german")
            language = input("Select language (default: english): ").strip() or "english"
            
            print("Select style:")
            print("1. Formal")
            print("2. Casual")
            style_choice = input("Enter choice (1-2): ").strip()
            formal = style_choice != "2"
            
            result = batch_greetings(names, language, formal)
            
            print(f"\n=== Batch Greetings ({language.title()}, {'Formal' if formal else 'Casual'}) ===")
            
            for name, greeting in result["greetings"].items():
                print(f"{name}: {greeting}")
            
            if "errors" in result:
                print("\nErrors:")
                for name, error in result["errors"].items():
                    print(f"{name}: {error}")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
