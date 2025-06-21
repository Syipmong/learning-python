"""
Week 4 - Exercise 4: Contact Book
Master dictionaries through a comprehensive contact management system.

Learning Goals:
- Create and manipulate dictionaries
- Use dictionary methods (keys(), values(), items())
- Work with nested dictionaries
- Implement search and filtering
- Practice data validation and organization

Tasks:
1. Create a contact book using dictionaries
2. Add, edit, and delete contacts
3. Search contacts by various criteria
4. Organize contacts into groups
5. Export/import contact data
6. Generate contact statistics
"""

import json
from datetime import datetime


def main():
    """
    Contact Book Manager
    
    Create a comprehensive contact management system using dictionaries
    to store and organize contact information.
    
    Requirements:
    - Store contacts as nested dictionaries
    - Support multiple contact methods (phone, email, address)
    - Implement search and filtering
    - Group contacts by categories
    - Validate contact information
    """
    contacts = {}
    groups = ["Family", "Friends", "Work", "Business", "Other"]
    
    print("📞 Contact Book Manager")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contacts")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Organize by groups")
        print("7. Generate statistics")
        print("8. Export/Import contacts")
        print("9. Exit")
        
        choice = input("\nSelect option (1-9): ").strip()
        
        if choice == "1":
            # TODO: Implement add_contact function
            pass
            
        elif choice == "2":
            # TODO: Implement view_all_contacts function
            pass
            
        elif choice == "3":
            # TODO: Implement search_contacts function
            pass
            
        elif choice == "4":
            # TODO: Implement edit_contact function
            pass
            
        elif choice == "5":
            # TODO: Implement delete_contact function
            pass
            
        elif choice == "6":
            # TODO: Implement organize_by_groups function
            pass
            
        elif choice == "7":
            # TODO: Implement generate_statistics function
            pass
            
        elif choice == "8":
            # TODO: Implement export_import_contacts function
            pass
            
        elif choice == "9":
            print("Goodbye! 📞")
            break
            
        else:
            print("Invalid option. Please try again.")


def add_contact(contacts, groups):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts (dict): Dictionary of all contacts
        groups (list): Available contact groups
    
    TODO: Implement this function
    - Get contact information (name, phone, email, address, etc.)
    - Create nested dictionary structure
    - Validate email format and phone number
    - Assign to group
    - Handle duplicate names
    """
    pass


def view_all_contacts(contacts):
    """
    Display all contacts in formatted way.
    
    Args:
        contacts (dict): Dictionary of all contacts
    
    TODO: Implement this function
    - Show all contacts with full details
    - Display in alphabetical order
    - Format output nicely (like a business card)
    - Show contact count
    - Handle empty contact book
    """
    pass


def search_contacts(contacts):
    """
    Search contacts by various criteria.
    
    Args:
        contacts (dict): Dictionary of all contacts
    
    TODO: Implement this function
    - Search by name (partial match)
    - Search by phone number
    - Search by email
    - Search by group
    - Search by city/state
    - Display search results
    """
    pass


def edit_contact(contacts):
    """
    Edit an existing contact.
    
    Args:
        contacts (dict): Dictionary of all contacts
    
    TODO: Implement this function
    - Show list of contacts to edit
    - Allow editing specific fields
    - Validate new information
    - Update contact dictionary
    - Show before/after comparison
    """
    pass


def delete_contact(contacts):
    """
    Delete a contact from the book.
    
    Args:
        contacts (dict): Dictionary of all contacts
    
    TODO: Implement this function
    - Show list of contacts
    - Confirm deletion
    - Remove from contacts dictionary
    - Show confirmation message
    """
    pass


def organize_by_groups(contacts):
    """
    Display contacts organized by groups.
    
    Args:
        contacts (dict): Dictionary of all contacts
    
    TODO: Implement this function
    - Group contacts by their assigned group
    - Display each group with its contacts
    - Show count per group
    - Allow moving contacts between groups
    """
    pass


def generate_statistics(contacts):
    """
    Generate and display contact book statistics.
    
    Args:
        contacts (dict): Dictionary of all contacts
    
    TODO: Implement this function
    - Total number of contacts
    - Contacts per group
    - Most common area codes
    - Contacts with missing information
    - Email domain statistics
    """
    pass


def export_import_contacts(contacts):
    """
    Export contacts to file or import from file.
    
    Args:
        contacts (dict): Dictionary of all contacts
    
    TODO: Implement this function
    - Export to JSON file
    - Import from JSON file
    - Export to CSV format
    - Handle file errors
    - Confirm operations
    """
    pass


def validate_email(email):
    """
    Validate email address format.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if valid, False otherwise
    
    TODO: Implement this function
    - Check for @ symbol
    - Check for domain
    - Basic format validation
    """
    pass


def validate_phone(phone):
    """
    Validate and format phone number.
    
    Args:
        phone (str): Phone number to validate
    
    Returns:
        str: Formatted phone number or None if invalid
    
    TODO: Implement this function
    - Remove non-digit characters
    - Check for valid length
    - Format as (XXX) XXX-XXXX
    """
    pass


def format_contact_display(name, contact_info):
    """
    Format contact information for display.
    
    Args:
        name (str): Contact name
        contact_info (dict): Contact details
    
    Returns:
        str: Formatted contact card
    
    TODO: Implement this function
    - Create business card style format
    - Handle missing information gracefully
    - Include all available contact methods
    """
    pass


if __name__ == "__main__":
    main()

# Example contact structure:
# contacts = {
#     "John Smith": {
#         "phone": "(555) 123-4567",
#         "email": "john.smith@email.com",
#         "address": {
#             "street": "123 Main St",
#             "city": "Anytown",
#             "state": "ST",
#             "zip": "12345"
#         },
#         "group": "Work",
#         "notes": "Manager at ABC Corp",
#         "birthday": "1985-03-15",
#         "created_date": "2024-01-15"
#     }
# }

# Expected behavior example:
#
# 📞 Contact Book Manager
# ========================================
# 
# Options:
# 1. Add contact
# 2. View all contacts
# 3. Search contacts
# 4. Edit contact
# 5. Delete contact
# 6. Organize by groups
# 7. Generate statistics
# 8. Export/Import contacts
# 9. Exit
# 
# Select option (1-9): 1
# Enter contact name: John Smith
# Enter phone number: 5551234567
# Enter email: john.smith@email.com
# Enter street address: 123 Main St
# Enter city: Anytown
# Enter state: ST
# Enter zip code: 12345
# Available groups: Family, Friends, Work, Business, Other
# Select group: Work
# Enter notes (optional): Manager at ABC Corp
# ✅ Contact 'John Smith' added successfully!
# 
# Select option (1-9): 2
# 📞 Contact Book (1 contact):
# 
# ╔════════════════════════════════════╗
# ║            JOHN SMITH              ║
# ╠════════════════════════════════════╣
# ║ 📞 (555) 123-4567                  ║
# ║ ✉️  john.smith@email.com           ║
# ║ 🏠 123 Main St                     ║
# ║    Anytown, ST 12345               ║
# ║ 👔 Work                            ║
# ║ 📝 Manager at ABC Corp             ║
# ╚════════════════════════════════════╝
