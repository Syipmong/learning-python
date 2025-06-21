"""
Week 4 - Exercise 5: Unique Word Counter
Learn sets and set operations through text analysis and word processing.

Learning Goals:
- Create and manipulate sets
- Use set operations (union, intersection, difference)
- Understand when to use sets vs other data structures
- Practice text processing and analysis
- Implement data deduplication

Tasks:
1. Analyze text to find unique words
2. Compare vocabulary between texts
3. Find common and unique words
4. Implement word filtering and cleaning
5. Generate vocabulary statistics
6. Create advanced text analysis tools
"""

import string
import re
from collections import Counter


def main():
    """
    Unique Word Counter and Text Analyzer
    
    Create a comprehensive text analysis tool using sets to find
    unique words, compare texts, and analyze vocabulary.
    
    Requirements:
    - Extract unique words from text
    - Compare vocabulary between multiple texts
    - Use set operations for analysis
    - Filter words by various criteria
    - Generate detailed statistics
    """
    texts = {}
    stop_words = load_common_stop_words()
    
    print("📝 Unique Word Counter & Text Analyzer")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Add text for analysis")
        print("2. View text summaries")
        print("3. Analyze unique words")
        print("4. Compare texts")
        print("5. Find word patterns")
        print("6. Filter and clean words")
        print("7. Generate vocabulary report")
        print("8. Exit")
        
        choice = input("\nSelect option (1-8): ").strip()
        
        if choice == "1":
            # TODO: Implement add_text function
            pass
            
        elif choice == "2":
            # TODO: Implement view_text_summaries function
            pass
            
        elif choice == "3":
            # TODO: Implement analyze_unique_words function
            pass
            
        elif choice == "4":
            # TODO: Implement compare_texts function
            pass
            
        elif choice == "5":
            # TODO: Implement find_word_patterns function
            pass
            
        elif choice == "6":
            # TODO: Implement filter_and_clean function
            pass
            
        elif choice == "7":
            # TODO: Implement generate_vocabulary_report function
            pass
            
        elif choice == "8":
            print("Happy analyzing! 📝")
            break
            
        else:
            print("Invalid option. Please try again.")


def add_text(texts):
    """
    Add text for analysis.
    
    Args:
        texts (dict): Dictionary storing text data
    
    TODO: Implement this function
    - Get text input (manual entry or file upload)
    - Store with unique identifier
    - Extract and store unique words as set
    - Calculate basic statistics
    - Handle different input methods
    """
    pass


def view_text_summaries(texts):
    """
    Display summaries of all stored texts.
    
    Args:
        texts (dict): Dictionary storing text data
    
    TODO: Implement this function
    - Show text names and basic info
    - Display word count, unique word count
    - Show text length and complexity
    - Preview first few sentences
    """
    pass


def analyze_unique_words(texts):
    """
    Analyze unique words in selected text.
    
    Args:
        texts (dict): Dictionary storing text data
    
    TODO: Implement this function
    - Show all unique words
    - Display words by length
    - Show alphabetically sorted unique words
    - Find longest and shortest words
    - Calculate vocabulary richness
    """
    pass


def compare_texts(texts):
    """
    Compare vocabulary between multiple texts.
    
    Args:
        texts (dict): Dictionary storing text data
    
    TODO: Implement this function
    - Select two or more texts to compare
    - Find common words (intersection)
    - Find unique words in each text (difference)
    - Find combined vocabulary (union)
    - Calculate similarity percentage
    """
    pass


def find_word_patterns(texts):
    """
    Find interesting word patterns in texts.
    
    Args:
        texts (dict): Dictionary storing text data
    
    TODO: Implement this function
    - Find words that start/end with specific letters
    - Find words of specific lengths
    - Find words containing specific patterns
    - Find palindromic words
    - Find compound words
    """
    pass


def filter_and_clean(texts, stop_words):
    """
    Filter and clean word sets.
    
    Args:
        texts (dict): Dictionary storing text data
        stop_words (set): Set of common stop words
    
    TODO: Implement this function
    - Remove stop words from analysis
    - Filter by word length
    - Remove punctuation and numbers
    - Convert to lowercase consistently
    - Create filtered word sets
    """
    pass


def generate_vocabulary_report(texts, stop_words):
    """
    Generate comprehensive vocabulary analysis report.
    
    Args:
        texts (dict): Dictionary storing text data
        stop_words (set): Set of common stop words
    
    TODO: Implement this function
    - Full vocabulary statistics
    - Word frequency analysis
    - Readability metrics
    - Vocabulary complexity scores
    - Export report option
    """
    pass


def extract_words_from_text(text):
    """
    Extract clean words from text.
    
    Args:
        text (str): Input text
    
    Returns:
        set: Set of unique words
    
    TODO: Implement this function
    - Remove punctuation
    - Convert to lowercase  
    - Split into words
    - Remove empty strings
    - Return as set
    """
    pass


def clean_word(word):
    """
    Clean a single word by removing punctuation and formatting.
    
    Args:
        word (str): Word to clean
    
    Returns:
        str: Cleaned word
    
    TODO: Implement this function
    - Remove leading/trailing punctuation
    - Convert to lowercase
    - Handle contractions
    - Remove numbers if needed
    """
    pass


def calculate_vocabulary_richness(total_words, unique_words):
    """
    Calculate vocabulary richness ratio.
    
    Args:
        total_words (int): Total word count
        unique_words (int): Unique word count
    
    Returns:
        float: Richness ratio (0-1)
    
    TODO: Implement this function
    - Calculate unique_words / total_words
    - Handle division by zero
    - Return as percentage
    """
    pass


def find_common_words(word_sets):
    """
    Find words common to all provided word sets.
    
    Args:
        word_sets (list): List of word sets
    
    Returns:
        set: Words common to all sets
    
    TODO: Implement this function
    - Use set intersection
    - Handle empty list case
    - Return intersection of all sets
    """
    pass


def find_unique_to_text(target_set, other_sets):
    """
    Find words unique to target set (not in any other set).
    
    Args:
        target_set (set): Target word set
        other_sets (list): Other word sets to compare against
    
    Returns:
        set: Words unique to target set
    
    TODO: Implement this function
    - Use set difference operation
    - Compare against union of other sets
    - Return unique words
    """
    pass


def load_common_stop_words():
    """
    Load common English stop words.
    
    Returns:
        set: Set of common stop words
    
    TODO: Implement this function
    - Define common stop words (the, and, or, but, etc.)
    - Return as set for fast lookup
    - Include articles, prepositions, conjunctions
    """
    pass


if __name__ == "__main__":
    main()

# Example text data structure:
# texts = {
#     "Sample Text 1": {
#         "content": "The quick brown fox jumps over the lazy dog.",
#         "words": {"the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"},
#         "word_count": 9,
#         "unique_count": 8,
#         "created_date": "2024-01-15"
#     }
# }

# Expected behavior example:
#
# 📝 Unique Word Counter & Text Analyzer
# ==================================================
# 
# Options:
# 1. Add text for analysis
# 2. View text summaries
# 3. Analyze unique words
# 4. Compare texts
# 5. Find word patterns
# 6. Filter and clean words
# 7. Generate vocabulary report
# 8. Exit
# 
# Select option (1-8): 1
# Enter text name: Sample Text
# Choose input method:
# 1. Type text manually
# 2. Load from file
# Select (1-2): 1
# Enter your text: The quick brown fox jumps over the lazy dog.
# ✅ Text 'Sample Text' added successfully!
# 
# 📊 Analysis Results:
# Total words: 9
# Unique words: 8
# Vocabulary richness: 88.9%
# 
# Select option (1-8): 3
# Available texts:
# 1. Sample Text
# Select text to analyze: 1
# 
# 📝 Unique Words in 'Sample Text':
# Alphabetical order: brown, dog, fox, jumps, lazy, over, quick, the
# By length:
#   3 letters: dog, fox, the
#   4 letters: lazy, over
#   5 letters: brown, jumps, quick
# 
# Longest word: brown, jumps, quick (5 letters)
# Shortest word: dog, fox, the (3 letters)
