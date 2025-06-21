"""
Week 4 - Exercise 1: Student Grade Manager
Learn list creation, indexing, and basic operations through a grade management system.

Learning Goals:
- Create and manipulate lists
- Use indexing and slicing
- Perform basic list operations
- Handle user input validation

Tasks:
1. Create a program that manages student grades
2. Allow adding grades to the list
3. Calculate average, highest, and lowest grades
4. Display grades in various formats
5. Remove specific grades
6. Find grades above/below certain thresholds
"""

def main():
    """
    Student Grade Manager
    
    Create a comprehensive grade management system that demonstrates
    list operations, indexing, and basic data manipulation.
    
    Requirements:
    - Store grades in a list
    - Validate grade input (0-100)
    - Calculate statistics (average, min, max)
    - Display grades in sorted order
    - Remove grades by value or index
    - Filter grades by criteria
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
            # TODO: Implement add_grade function
            # Should validate input (0-100) and add to grades list
            pass
            
        elif choice == "2":
            # TODO: Implement view_grades function
            # Should display grades in original order and sorted order
            pass
            
        elif choice == "3":
            # TODO: Implement calculate_statistics function
            # Should show average, highest, lowest, count
            pass
            
        elif choice == "4":
            # TODO: Implement remove_grade function
            # Should allow removal by value or index
            pass
            
        elif choice == "5":
            # TODO: Implement filter_grades function
            # Should show grades above/below threshold
            pass
            
        elif choice == "6":
            print("Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")


def add_grade(grades):
    """
    Add a grade to the list with validation.
    
    Args:
        grades (list): List of grades to add to
    
    TODO: Implement this function
    - Get grade input from user
    - Validate grade is between 0 and 100
    - Add valid grade to list
    - Show confirmation message
    """
    pass


def view_grades(grades):
    """
    Display grades in various formats.
    
    Args:
        grades (list): List of grades to display
    
    TODO: Implement this function
    - Show all grades in original order
    - Show all grades in sorted order (ascending and descending)
    - Show grades with index numbers
    - Handle empty list case
    """
    pass


def calculate_statistics(grades):
    """
    Calculate and display grade statistics.
    
    Args:
        grades (list): List of grades to analyze
    
    TODO: Implement this function
    - Calculate average grade
    - Find highest and lowest grades
    - Count total grades
    - Show letter grade distribution (A, B, C, D, F)
    - Handle empty list case
    """
    pass


def remove_grade(grades):
    """
    Remove a grade from the list by value or index.
    
    Args:
        grades (list): List of grades to remove from
    
    TODO: Implement this function
    - Ask user to remove by value or index
    - Handle removal by specific grade value
    - Handle removal by index position
    - Show updated list after removal
    - Handle invalid inputs and empty list
    """
    pass


def filter_grades(grades):
    """
    Filter and display grades based on criteria.
    
    Args:
        grades (list): List of grades to filter
    
    TODO: Implement this function
    - Show grades above a threshold
    - Show grades below a threshold
    - Show grades in a specific range
    - Show passing grades (>= 60)
    - Show failing grades (< 60)
    """
    pass


if __name__ == "__main__":
    main()

# Example expected behavior:
# 
# 🎓 Student Grade Manager
# ========================================
# 
# Options:
# 1. Add grade
# 2. View all grades
# 3. Calculate statistics
# 4. Remove grade
# 5. Filter grades
# 6. Exit
# 
# Select option (1-6): 1
# Enter grade (0-100): 85
# ✅ Grade 85 added successfully!
# 
# Select option (1-6): 1
# Enter grade (0-100): 92
# ✅ Grade 92 added successfully!
# 
# Select option (1-6): 3
# 📊 Grade Statistics:
# Average: 88.50
# Highest: 92
# Lowest: 85
# Total grades: 2
# 
# Letter Grade Distribution:
# A (90-100): 1 grade(s)
# B (80-89): 1 grade(s)
# C (70-79): 0 grade(s)
# D (60-69): 0 grade(s)
# F (0-59): 0 grade(s)
