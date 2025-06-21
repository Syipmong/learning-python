# Solution 2: Grade Calculator

try:
    score = float(input("Enter your numerical score (0-100): "))
    
    # Validate score
    if score < 0 or score > 100:
        print("Error: Score must be between 0 and 100!")
    else:
        # Determine letter grade and feedback
        if score >= 90:
            letter_grade = "A"
            feedback = "Excellent work!"
            gpa_points = 4.0
        elif score >= 80:
            letter_grade = "B"
            feedback = "Good job!"
            gpa_points = 3.0
        elif score >= 70:
            letter_grade = "C"
            feedback = "Satisfactory"
            gpa_points = 2.0
        elif score >= 60:
            letter_grade = "D"
            feedback = "Needs improvement"
            gpa_points = 1.0
        else:  # score < 60
            letter_grade = "F"
            feedback = "Please see instructor"
            gpa_points = 0.0
        
        # Display results
        print(f"\n📊 GRADE REPORT")
        print(f"{'='*30}")
        print(f"Numerical Score: {score:.1f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA Points: {gpa_points}")
        print(f"Feedback: {feedback}")
        
        # Additional insights
        if score >= 97:
            print("🌟 Outstanding performance!")
        elif score >= 93:
            print("⭐ Excellent work!")
        elif score == 100:
            print("🏆 Perfect score! Amazing!")
        
        # Grade boundary information
        if letter_grade == "B" and score >= 87:
            points_to_A = 90 - score
            print(f"💡 You're only {points_to_A:.1f} points away from an A!")
        elif letter_grade == "C" and score >= 77:
            points_to_B = 80 - score
            print(f"💡 You're only {points_to_B:.1f} points away from a B!")
        elif letter_grade == "D" and score >= 67:
            points_to_C = 70 - score
            print(f"💡 You're only {points_to_C:.1f} points away from a C!")
        elif letter_grade == "F" and score >= 55:
            points_to_D = 60 - score
            print(f"💡 You need {points_to_D:.1f} more points to pass!")
        
        # Percentage display
        print(f"📈 Percentage: {score}%")
        
        # Pass/Fail status
        if score >= 60:
            print("✅ Status: PASS")
        else:
            print("❌ Status: FAIL")

except ValueError:
    print("Error: Please enter a valid number!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
