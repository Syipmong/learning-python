# Solution 5: Personal Information Collector (Weekend Project)

from datetime import datetime

print("=== Personal Information Collector ===")
print("Please provide the following information:\n")

# Collect information with error handling
try:
    # Basic information
    full_name = input("Enter your full name: ").strip()
    
    # Age with validation
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 150:
                print("Please enter a valid age between 0 and 150.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for age.")
    
    city = input("Enter your city: ").strip()
    favorite_color = input("Enter your favorite color: ").strip()
    
    # Favorite number with validation
    while True:
        try:
            favorite_number = int(input("Enter your favorite number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Email with basic validation
    while True:
        email = input("Enter your email address: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print("Please enter a valid email address (must contain @ and .)")
    
    # Optional phone number
    phone = input("Enter your phone number (optional): ").strip()
    if not phone:
        phone = "Not provided"

    # Calculate statistics
    current_year = datetime.now().year
    birth_year = current_year - age
    days_lived = age * 365  # Approximate
    
    # Extract initials
    name_parts = full_name.split()
    initials = "".join([part[0].upper() for part in name_parts if part])
    
    # Extract email username
    email_username = email.split("@")[0]
    
    # Create formatted display
    print("\n" + "="*50)
    print("╔══════════════════════════════════════════════════╗")
    print("║                PERSONAL PROFILE                  ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║ Name: {full_name:<25} ({initials:<4})        ║")
    print(f"║ Age: {age} years (born ~{birth_year})                    ║")
    print(f"║ Location: {city:<35}      ║")
    print(f"║ Contact: {email:<32}      ║")
    if phone != "Not provided":
        print(f"║ Phone: {phone:<37}      ║")
    print(f"║ Favorites: {favorite_color}, Number {favorite_number:<20}      ║")
    print(f"║ Days Lived: ~{days_lived:,} days{' '*(25-len(str(days_lived)))}║")
    print(f"║ Email Username: {email_username:<27}      ║")
    print("╚══════════════════════════════════════════════════╝")
    
    # Additional fun facts
    print(f"\n🎉 Fun Facts about {name_parts[0]}:")
    print(f"   • You've been alive for approximately {days_lived * 24:,} hours!")
    print(f"   • Your name has {len(full_name.replace(' ', ''))} characters (without spaces)")
    print(f"   • You were born in the {birth_year}s")
    print(f"   • Your initials spell: {initials}")
    
    # Name analysis
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in full_name if char in vowels)
    consonant_count = sum(1 for char in full_name if char.isalpha() and char not in vowels)
    
    print(f"   • Your name contains {vowel_count} vowels and {consonant_count} consonants")
    
    if len(full_name) > 15:
        print(f"   • You have a long name! ({len(full_name)} characters)")
    
    # Lucky number calculation
    lucky_number = (age + favorite_number) % 10
    print(f"   • Your lucky number today is: {lucky_number}")
    
    print(f"\nThank you for using the Personal Information Collector!")
    print("Your information has been processed successfully! 🎊")

except KeyboardInterrupt:
    print("\n\nProgram interrupted by user. Goodbye!")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
    print("Please try running the program again.")
