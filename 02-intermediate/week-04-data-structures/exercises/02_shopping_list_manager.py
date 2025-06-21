"""
Week 4 - Exercise 2: Shopping List Manager
Master list methods and manipulation through a shopping list application.

Learning Goals:
- Use list methods (append, insert, remove, pop, etc.)
- Understand list modification operations
- Practice string manipulation with lists
- Implement search and organization features

Tasks:
1. Create a shopping list manager
2. Add items with quantities and categories
3. Mark items as purchased
4. Organize items by category
5. Calculate estimated costs
6. Generate shopping summary
"""

def main():
    """
    Shopping List Manager
    
    Create a comprehensive shopping list application that demonstrates
    advanced list operations and methods.
    
    Requirements:
    - Store items as dictionaries in a list
    - Add, remove, and modify items
    - Organize by categories
    - Track purchased status
    - Calculate totals and summaries
    """
    shopping_list = []
    categories = ["Produce", "Dairy", "Meat", "Bakery", "Pantry", "Frozen", "Other"]
    
    print("🛒 Shopping List Manager")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. View shopping list")
        print("3. Mark item as purchased")
        print("4. Remove item")
        print("5. Organize by category")
        print("6. Calculate totals")
        print("7. Generate shopping summary")
        print("8. Exit")
        
        choice = input("\nSelect option (1-8): ").strip()
        
        if choice == "1":
            # TODO: Implement add_item function
            pass
            
        elif choice == "2":
            # TODO: Implement view_shopping_list function
            pass
            
        elif choice == "3":
            # TODO: Implement mark_purchased function
            pass
            
        elif choice == "4":
            # TODO: Implement remove_item function
            pass
            
        elif choice == "5":
            # TODO: Implement organize_by_category function
            pass
            
        elif choice == "6":
            # TODO: Implement calculate_totals function
            pass
            
        elif choice == "7":
            # TODO: Implement generate_summary function
            pass
            
        elif choice == "8":
            print("Happy shopping! 🛍️")
            break
            
        else:
            print("Invalid option. Please try again.")


def add_item(shopping_list, categories):
    """
    Add an item to the shopping list.
    
    Args:
        shopping_list (list): List of shopping items
        categories (list): Available categories
    
    TODO: Implement this function
    - Get item name, quantity, estimated price, and category
    - Create item dictionary with all details
    - Add to shopping list
    - Handle duplicate items (ask to update or add separately)
    """
    pass


def view_shopping_list(shopping_list):
    """
    Display the shopping list in various formats.
    
    Args:
        shopping_list (list): List of shopping items
    
    TODO: Implement this function
    - Show all items with details
    - Separate purchased and unpurchased items
    - Display in table format
    - Show total item count
    """
    pass


def mark_purchased(shopping_list):
    """
    Mark items as purchased.
    
    Args:
        shopping_list (list): List of shopping items
    
    TODO: Implement this function
    - Show unpurchased items
    - Allow user to select item to mark
    - Update purchased status
    - Show confirmation
    """
    pass


def remove_item(shopping_list):
    """
    Remove an item from the shopping list.
    
    Args:
        shopping_list (list): List of shopping items
    
    TODO: Implement this function
    - Show all items with index numbers
    - Allow removal by index or name
    - Confirm removal
    - Handle invalid selections
    """
    pass


def organize_by_category(shopping_list):
    """
    Display items organized by category.
    
    Args:
        shopping_list (list): List of shopping items
    
    TODO: Implement this function
    - Group items by category
    - Display each category with its items
    - Show count per category
    - Sort categories alphabetically
    """
    pass


def calculate_totals(shopping_list):
    """
    Calculate and display cost totals.
    
    Args:
        shopping_list (list): List of shopping items
    
    TODO: Implement this function
    - Calculate total estimated cost
    - Calculate cost of purchased items
    - Calculate remaining cost
    - Show breakdown by category
    """
    pass


def generate_summary(shopping_list):
    """
    Generate and display shopping summary.
    
    Args:
        shopping_list (list): List of shopping items
    
    TODO: Implement this function
    - Show total items and categories
    - Show purchase progress
    - Show most/least expensive items
    - Generate formatted shopping list for printing
    """
    pass


if __name__ == "__main__":
    main()

# Example item structure:
# {
#     'name': 'Apples',
#     'quantity': '2 lbs',
#     'category': 'Produce',
#     'estimated_price': 3.50,
#     'purchased': False,
#     'notes': 'Red delicious'
# }

# Expected behavior example:
# 
# 🛒 Shopping List Manager
# ========================================
# 
# Options:
# 1. Add item
# 2. View shopping list
# 3. Mark item as purchased
# 4. Remove item
# 5. Organize by category
# 6. Calculate totals
# 7. Generate shopping summary
# 8. Exit
# 
# Select option (1-8): 1
# Enter item name: Milk
# Enter quantity: 1 gallon
# Available categories: Produce, Dairy, Meat, Bakery, Pantry, Frozen, Other
# Select category: Dairy
# Enter estimated price: $3.99
# Enter notes (optional): Whole milk
# ✅ Added 'Milk' to shopping list!
# 
# Select option (1-8): 2
# 🛒 Shopping List (1 item):
# 
# UNPURCHASED ITEMS:
# 1. Milk (1 gallon) - Dairy - $3.99 [Whole milk]
# 
# PURCHASED ITEMS:
# None
# 
# Total items: 1 | Purchased: 0 | Remaining: 1
