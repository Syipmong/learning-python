# Solution 1: Age Category Classifier

try:
    age = int(input("Enter your age: "))
    
    # Validate age input
    if age < 0:
        print("Age cannot be negative!")
    elif age > 150:
        print("Please enter a realistic age!")
    else:
        # Classify age into categories
        if age <= 2:
            category = "Toddler"
            info = "You're just starting to explore the world! 👶"
        elif age <= 12:
            category = "Child"
            info = "Time for learning and playing! 🎈"
        elif age <= 19:
            category = "Teenager"
            info = "The exciting teenage years! 🎸"
        elif age <= 64:
            category = "Adult"
            info = "The productive years of life! 💼"
        else:  # age >= 65
            category = "Senior"
            info = "Wisdom and experience! 👴👵"
        
        print(f"\nYou are a {category}.")
        print(info)
        
        # Additional fun facts
        if age == 18:
            print("🎉 You've just reached adulthood!")
        elif age == 21:
            print("🎉 Welcome to full adulthood!")
        elif age in [30, 40, 50, 60, 70, 80, 90, 100]:
            print(f"🎂 Milestone birthday! You're {age}!")
        
        # Life stage insights
        if age < 18:
            years_to_18 = 18 - age
            print(f"📅 You'll be an adult in {years_to_18} year(s)!")
        elif age >= 18 and age < 65:
            years_to_retirement = 65 - age
            print(f"⏰ Estimated years to retirement: {years_to_retirement}")

except ValueError:
    print("Please enter a valid number for age!")
except Exception as e:
    print(f"An error occurred: {e}")
