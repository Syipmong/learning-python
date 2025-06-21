"""
Week 4 - Exercise 1: Student Grade Manager (Solution)
Comprehensive grade management system demonstrating list operations and data manipulation.
"""


def main():
    """
    Student Grade Manager - Complete Solution
    
    Demonstrates list creation, indexing, slicing, and manipulation
    through a comprehensive grade management system.
    """
    grades = []
    
    print("🎓 Student Grade Manager")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Add grade")
        print("2. View all grades")
        print("3. Calculate statistics")
        print("4. Remove grade")
        print("5. Filter grades")
        print("6. Exit")
        
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == "1":
            add_grade(grades)
        elif choice == "2":
            view_grades(grades)
        elif choice == "3":
            calculate_statistics(grades)
        elif choice == "4":
            remove_grade(grades)
        elif choice == "5":
            filter_grades(grades)
        elif choice == "6":
            print("Goodbye! 🎓")
            break
        else:
            print("❌ Invalid option. Please try again.")


def add_grade(grades):
    """
    Add a grade to the list with validation.
    
    Args:
        grades (list): List of grades to add to
    """
    try:
        grade_input = input("Enter grade (0-100): ").strip()
        
        # Handle empty input
        if not grade_input:
            print("❌ Please enter a grade.")
            return
        
        grade = float(grade_input)
        
        # Validate grade range
        if grade < 0 or grade > 100:
            print("❌ Grade must be between 0 and 100.")
            return
        
        grades.append(grade)
        print(f"✅ Grade {grade} added successfully!")
        print(f"📊 Total grades: {len(grades)}")
        
    except ValueError:
        print("❌ Please enter a valid number.")


def view_grades(grades):
    """
    Display grades in various formats.
    
    Args:
        grades (list): List of grades to display
    """
    if not grades:
        print("📝 No grades recorded yet.")
        return
    
    print(f"\n📊 Grade Summary ({len(grades)} grades)")
    print("=" * 40)
    
    # Display grades in original order
    print("\n📝 Grades (Original Order):")
    for i, grade in enumerate(grades, 1):
        letter_grade = get_letter_grade(grade)
        print(f"{i:2d}. {grade:5.1f} ({letter_grade})")
    
    # Display grades in sorted order
    sorted_grades = sorted(grades)
    print("\n📈 Grades (Sorted - Lowest to Highest):")
    for i, grade in enumerate(sorted_grades, 1):
        letter_grade = get_letter_grade(grade)
        print(f"{i:2d}. {grade:5.1f} ({letter_grade})")
    
    # Display grades in reverse sorted order
    reverse_sorted_grades = sorted(grades, reverse=True)
    print("\n📉 Grades (Sorted - Highest to Lowest):")
    for i, grade in enumerate(reverse_sorted_grades, 1):
        letter_grade = get_letter_grade(grade)
        print(f"{i:2d}. {grade:5.1f} ({letter_grade})")


def calculate_statistics(grades):
    """
    Calculate and display grade statistics.
    
    Args:
        grades (list): List of grades to analyze
    """
    if not grades:
        print("📝 No grades recorded yet.")
        return
    
    # Basic statistics
    total_grades = len(grades)
    average = sum(grades) / total_grades
    highest = max(grades)
    lowest = min(grades)
    grade_range = highest - lowest
    
    print(f"\n📊 Grade Statistics")
    print("=" * 40)
    print(f"Total grades:     {total_grades}")
    print(f"Average grade:    {average:.2f} ({get_letter_grade(average)})")
    print(f"Highest grade:    {highest:.1f} ({get_letter_grade(highest)})")
    print(f"Lowest grade:     {lowest:.1f} ({get_letter_grade(lowest)})")
    print(f"Grade range:      {grade_range:.1f}")
    
    # Calculate median
    sorted_grades = sorted(grades)
    if total_grades % 2 == 0:
        median = (sorted_grades[total_grades//2 - 1] + sorted_grades[total_grades//2]) / 2
    else:
        median = sorted_grades[total_grades//2]
    
    print(f"Median grade:     {median:.2f} ({get_letter_grade(median)})")
    
    # Letter grade distribution
    print(f"\n📋 Letter Grade Distribution:")
    letter_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for grade in grades:
        letter = get_letter_grade(grade)
        letter_counts[letter] += 1
    
    for letter, count in letter_counts.items():
        percentage = (count / total_grades) * 100
        bar = "█" * (count * 2) if count > 0 else ""
        print(f"{letter} (90-100): {count:2d} grade(s) ({percentage:4.1f}%) {bar}")
    
    # Passing/Failing statistics
    passing_grades = [g for g in grades if g >= 60]
    failing_grades = [g for g in grades if g < 60]
    
    print(f"\n✅ Passing grades (≥60): {len(passing_grades)} ({len(passing_grades)/total_grades*100:.1f}%)")
    print(f"❌ Failing grades (<60): {len(failing_grades)} ({len(failing_grades)/total_grades*100:.1f}%)")


def remove_grade(grades):
    """
    Remove a grade from the list by value or index.
    
    Args:
        grades (list): List of grades to remove from
    """
    if not grades:
        print("📝 No grades recorded yet.")
        return
    
    print("\nRemove grade by:")
    print("1. Grade value")
    print("2. Position (index)")
    
    choice = input("Select option (1-2): ").strip()
    
    if choice == "1":
        remove_by_value(grades)
    elif choice == "2":
        remove_by_index(grades)
    else:
        print("❌ Invalid option.")


def remove_by_value(grades):
    """Remove grade by specific value."""
    try:
        grade_to_remove = float(input("Enter grade to remove: "))
        
        if grade_to_remove in grades:
            grades.remove(grade_to_remove)
            print(f"✅ Grade {grade_to_remove} removed successfully!")
            print(f"📊 Remaining grades: {len(grades)}")
        else:
            print(f"❌ Grade {grade_to_remove} not found in the list.")
            
    except ValueError:
        print("❌ Please enter a valid number.")


def remove_by_index(grades):
    """Remove grade by index position."""
    # Show grades with index numbers
    print("\nCurrent grades:")
    for i, grade in enumerate(grades):
        print(f"{i+1}. {grade}")
    
    try:
        index = int(input(f"Enter position to remove (1-{len(grades)}): ")) - 1
        
        if 0 <= index < len(grades):
            removed_grade = grades.pop(index)
            print(f"✅ Grade {removed_grade} removed from position {index + 1}!")
            print(f"📊 Remaining grades: {len(grades)}")
        else:
            print(f"❌ Invalid position. Please enter a number between 1 and {len(grades)}.")
            
    except ValueError:
        print("❌ Please enter a valid number.")


def filter_grades(grades):
    """
    Filter and display grades based on criteria.
    
    Args:
        grades (list): List of grades to filter
    """
    if not grades:
        print("📝 No grades recorded yet.")
        return
    
    print("\nFilter options:")
    print("1. Grades above threshold")
    print("2. Grades below threshold")
    print("3. Grades in range")
    print("4. Passing grades (≥60)")
    print("5. Failing grades (<60)")
    print("6. Grades by letter grade")
    
    choice = input("Select filter option (1-6): ").strip()
    
    if choice == "1":
        filter_above_threshold(grades)
    elif choice == "2":
        filter_below_threshold(grades)
    elif choice == "3":
        filter_in_range(grades)
    elif choice == "4":
        filter_passing_grades(grades)
    elif choice == "5":
        filter_failing_grades(grades)
    elif choice == "6":
        filter_by_letter_grade(grades)
    else:
        print("❌ Invalid option.")


def filter_above_threshold(grades):
    """Show grades above a threshold."""
    try:
        threshold = float(input("Enter minimum grade: "))
        filtered_grades = [g for g in grades if g >= threshold]
        
        if filtered_grades:
            print(f"\n📈 Grades ≥ {threshold}:")
            for grade in sorted(filtered_grades, reverse=True):
                print(f"  {grade:.1f} ({get_letter_grade(grade)})")
            print(f"\nFound {len(filtered_grades)} out of {len(grades)} grades.")
        else:
            print(f"❌ No grades found ≥ {threshold}.")
            
    except ValueError:
        print("❌ Please enter a valid number.")


def filter_below_threshold(grades):
    """Show grades below a threshold."""
    try:
        threshold = float(input("Enter maximum grade: "))
        filtered_grades = [g for g in grades if g <= threshold]
        
        if filtered_grades:
            print(f"\n📉 Grades ≤ {threshold}:")
            for grade in sorted(filtered_grades, reverse=True):
                print(f"  {grade:.1f} ({get_letter_grade(grade)})")
            print(f"\nFound {len(filtered_grades)} out of {len(grades)} grades.")
        else:
            print(f"❌ No grades found ≤ {threshold}.")
            
    except ValueError:
        print("❌ Please enter a valid number.")


def filter_in_range(grades):
    """Show grades within a range."""
    try:
        min_grade = float(input("Enter minimum grade: "))
        max_grade = float(input("Enter maximum grade: "))
        
        if min_grade > max_grade:
            min_grade, max_grade = max_grade, min_grade
        
        filtered_grades = [g for g in grades if min_grade <= g <= max_grade]
        
        if filtered_grades:
            print(f"\n📊 Grades between {min_grade} and {max_grade}:")
            for grade in sorted(filtered_grades, reverse=True):
                print(f"  {grade:.1f} ({get_letter_grade(grade)})")
            print(f"\nFound {len(filtered_grades)} out of {len(grades)} grades.")
        else:
            print(f"❌ No grades found between {min_grade} and {max_grade}.")
            
    except ValueError:
        print("❌ Please enter valid numbers.")


def filter_passing_grades(grades):
    """Show passing grades (≥60)."""
    passing_grades = [g for g in grades if g >= 60]
    
    if passing_grades:
        print(f"\n✅ Passing Grades (≥60):")
        for grade in sorted(passing_grades, reverse=True):
            print(f"  {grade:.1f} ({get_letter_grade(grade)})")
        print(f"\nFound {len(passing_grades)} out of {len(grades)} grades.")
    else:
        print("❌ No passing grades found.")


def filter_failing_grades(grades):
    """Show failing grades (<60)."""
    failing_grades = [g for g in grades if g < 60]
    
    if failing_grades:
        print(f"\n❌ Failing Grades (<60):")
        for grade in sorted(failing_grades, reverse=True):
            print(f"  {grade:.1f} ({get_letter_grade(grade)})")
        print(f"\nFound {len(failing_grades)} out of {len(grades)} grades.")
    else:
        print("✅ No failing grades found.")


def filter_by_letter_grade(grades):
    """Filter grades by letter grade."""
    print("\nSelect letter grade:")
    print("A. 90-100")
    print("B. 80-89")
    print("C. 70-79")
    print("D. 60-69")
    print("F. 0-59")
    
    letter = input("Enter letter grade (A-F): ").strip().upper()
    
    if letter not in ['A', 'B', 'C', 'D', 'F']:
        print("❌ Invalid letter grade.")
        return
    
    # Define grade ranges
    ranges = {
        'A': (90, 100),
        'B': (80, 89.99),
        'C': (70, 79.99),
        'D': (60, 69.99),
        'F': (0, 59.99)
    }
    
    min_grade, max_grade = ranges[letter]
    filtered_grades = [g for g in grades if min_grade <= g <= max_grade]
    
    if filtered_grades:
        print(f"\n📊 {letter} Grades ({min_grade}-{max_grade:.0f}):")
        for grade in sorted(filtered_grades, reverse=True):
            print(f"  {grade:.1f}")
        print(f"\nFound {len(filtered_grades)} out of {len(grades)} grades.")
    else:
        print(f"❌ No {letter} grades found.")


def get_letter_grade(grade):
    """
    Convert numeric grade to letter grade.
    
    Args:
        grade (float): Numeric grade
    
    Returns:
        str: Letter grade
    """
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    main()
