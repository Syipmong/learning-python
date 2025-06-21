"""
Week 4 - Weekend Project: Data Analysis Tool
Comprehensive data analysis application using all data structures learned this week.

Learning Goals:
- Integrate lists, tuples, dictionaries, and sets
- Build a complete data analysis pipeline
- Practice file I/O and data processing
- Implement statistical analysis
- Create data visualization (text-based)

Project Requirements:
1. Load data from CSV files or manual input
2. Clean and process data using appropriate data structures
3. Perform statistical analysis
4. Generate reports and visualizations
5. Export results to files
6. Create an interactive interface

This project combines all Week 4 concepts into a practical application.
"""

import csv
import json
import statistics
from datetime import datetime
from collections import Counter, defaultdict


def main():
    """
    Data Analysis Tool - Weekend Project
    
    A comprehensive tool that demonstrates mastery of all data structures
    learned in Week 4: lists, tuples, dictionaries, and sets.
    
    Features:
    - Data loading and cleaning
    - Statistical analysis
    - Data visualization (text-based)
    - Report generation
    - Data export capabilities
    """
    datasets = {}  # Dictionary to store multiple datasets
    analysis_results = []  # List to store analysis results
    
    print("📊 Data Analysis Tool - Weekend Project")
    print("=" * 50)
    
    while True:
        print("\n🔧 MAIN MENU")
        print("1. 📁 Data Management")
        print("2. 🧹 Data Cleaning")
        print("3. 📈 Statistical Analysis")
        print("4. 📊 Data Visualization")
        print("5. 📋 Generate Reports")
        print("6. 💾 Export Data")
        print("7. ❌ Exit")
        
        choice = input("\nSelect option (1-7): ").strip()
        
        if choice == "1":
            data_management_menu(datasets)
        elif choice == "2":
            data_cleaning_menu(datasets)
        elif choice == "3":
            statistical_analysis_menu(datasets, analysis_results)
        elif choice == "4":
            visualization_menu(datasets)
        elif choice == "5":
            generate_reports_menu(datasets, analysis_results)
        elif choice == "6":
            export_data_menu(datasets, analysis_results)
        elif choice == "7":
            print("Thank you for using the Data Analysis Tool! 📊")
            break
        else:
            print("❌ Invalid option. Please try again.")


def data_management_menu(datasets):
    """
    Handle data loading, viewing, and basic management.
    
    Args:
        datasets (dict): Dictionary containing all loaded datasets
    
    TODO: Implement comprehensive data management
    - Load CSV files
    - Manual data entry
    - View dataset summaries
    - Delete datasets
    - Rename datasets
    """
    print("\n📁 DATA MANAGEMENT")
    print("1. Load CSV file")
    print("2. Create dataset manually")
    print("3. View datasets")
    print("4. Delete dataset")
    print("5. Back to main menu")
    
    choice = input("\nSelect option (1-5): ").strip()
    
    if choice == "1":
        # TODO: Implement load_csv_file function
        pass
    elif choice == "2":
        # TODO: Implement create_manual_dataset function
        pass
    elif choice == "3":
        # TODO: Implement view_datasets function
        pass
    elif choice == "4":
        # TODO: Implement delete_dataset function
        pass


def data_cleaning_menu(datasets):
    """
    Handle data cleaning and preprocessing.
    
    Args:
        datasets (dict): Dictionary containing all loaded datasets
    
    TODO: Implement data cleaning features
    - Remove duplicates (using sets)
    - Handle missing values
    - Standardize data formats
    - Filter data by criteria
    - Validate data types
    """
    print("\n🧹 DATA CLEANING")
    print("1. Remove duplicates")
    print("2. Handle missing values")
    print("3. Standardize formats")
    print("4. Filter data")
    print("5. Validate data types")
    print("6. Back to main menu")
    
    choice = input("\nSelect option (1-6): ").strip()
    
    # TODO: Implement each cleaning option
    pass


def statistical_analysis_menu(datasets, analysis_results):
    """
    Perform statistical analysis on datasets.
    
    Args:
        datasets (dict): Dictionary containing all loaded datasets
        analysis_results (list): List to store analysis results
    
    TODO: Implement statistical analysis features
    - Descriptive statistics (mean, median, mode, etc.)
    - Correlation analysis
    - Frequency analysis
    - Trend analysis
    - Comparative analysis between datasets
    """
    print("\n📈 STATISTICAL ANALYSIS")
    print("1. Descriptive statistics")
    print("2. Frequency analysis")
    print("3. Correlation analysis")
    print("4. Compare datasets")
    print("5. Custom analysis")
    print("6. Back to main menu")
    
    choice = input("\nSelect option (1-6): ").strip()
    
    # TODO: Implement each analysis option
    pass


def visualization_menu(datasets):
    """
    Create text-based visualizations of data.
    
    Args:
        datasets (dict): Dictionary containing all loaded datasets
    
    TODO: Implement visualization features
    - Bar charts (ASCII)
    - Histograms
    - Scatter plots (text-based)
    - Pie charts
    - Line graphs
    """
    print("\n📊 DATA VISUALIZATION")
    print("1. Bar chart")
    print("2. Histogram")
    print("3. Scatter plot")
    print("4. Pie chart")
    print("5. Line graph")
    print("6. Back to main menu")
    
    choice = input("\nSelect option (1-6): ").strip()
    
    # TODO: Implement each visualization option
    pass


def generate_reports_menu(datasets, analysis_results):
    """
    Generate comprehensive reports.
    
    Args:
        datasets (dict): Dictionary containing all loaded datasets
        analysis_results (list): List of analysis results
    
    TODO: Implement report generation
    - Summary reports
    - Detailed analysis reports
    - Comparison reports
    - Custom reports
    - Save reports to files
    """
    print("\n📋 GENERATE REPORTS")
    print("1. Summary report")
    print("2. Detailed analysis report")
    print("3. Comparison report")
    print("4. Custom report")
    print("5. Back to main menu")
    
    choice = input("\nSelect option (1-5): ").strip()
    
    # TODO: Implement each report type
    pass


def export_data_menu(datasets, analysis_results):
    """
    Export data and results to various formats.
    
    Args:
        datasets (dict): Dictionary containing all loaded datasets
        analysis_results (list): List of analysis results
    
    TODO: Implement export functionality
    - Export to CSV
    - Export to JSON
    - Export analysis results
    - Export visualizations
    - Batch export
    """
    print("\n💾 EXPORT DATA")
    print("1. Export dataset to CSV")
    print("2. Export dataset to JSON")
    print("3. Export analysis results")
    print("4. Export all data")
    print("5. Back to main menu")
    
    choice = input("\nSelect option (1-5): ").strip()
    
    # TODO: Implement each export option
    pass


# Data Loading Functions
def load_csv_file(datasets):
    """
    Load data from CSV file.
    
    Args:
        datasets (dict): Dictionary to store the loaded dataset
    
    TODO: Implement CSV loading
    - Get filename from user
    - Read CSV file
    - Store as list of dictionaries
    - Handle headers
    - Validate data
    """
    pass


def create_manual_dataset(datasets):
    """
    Create dataset through manual input.
    
    Args:
        datasets (dict): Dictionary to store the created dataset
    
    TODO: Implement manual dataset creation
    - Get dataset name
    - Define columns
    - Enter data row by row
    - Store in appropriate structure
    """
    pass


# Data Cleaning Functions
def remove_duplicates(dataset):
    """
    Remove duplicate records from dataset using sets.
    
    Args:
        dataset (list): List of dictionaries representing data
    
    Returns:
        list: Dataset with duplicates removed
    
    TODO: Implement duplicate removal
    - Convert records to tuples for set operations
    - Use set to find unique records
    - Return cleaned dataset
    """
    pass


def handle_missing_values(dataset):
    """
    Handle missing values in dataset.
    
    Args:
        dataset (list): List of dictionaries representing data
    
    Returns:
        list: Dataset with missing values handled
    
    TODO: Implement missing value handling
    - Detect missing values (None, empty strings, etc.)
    - Options: remove, fill with mean/median, interpolate
    - Return cleaned dataset
    """
    pass


# Statistical Analysis Functions
def calculate_descriptive_stats(data_column):
    """
    Calculate descriptive statistics for a data column.
    
    Args:
        data_column (list): List of numeric values
    
    Returns:
        dict: Dictionary containing statistical measures
    
    TODO: Implement statistical calculations
    - Mean, median, mode
    - Standard deviation, variance
    - Min, max, range
    - Quartiles
    - Return as dictionary
    """
    pass


def frequency_analysis(data_column):
    """
    Perform frequency analysis on data column.
    
    Args:
        data_column (list): List of values to analyze
    
    Returns:
        dict: Frequency counts
    
    TODO: Implement frequency analysis
    - Use Counter from collections
    - Calculate frequencies
    - Find most/least common values
    - Return frequency distribution
    """
    pass


# Visualization Functions
def create_ascii_bar_chart(data, title="Bar Chart"):
    """
    Create ASCII bar chart from data.
    
    Args:
        data (dict): Dictionary with labels and values
        title (str): Chart title
    
    TODO: Implement ASCII bar chart
    - Scale values to fit terminal width
    - Use characters to represent bars
    - Add labels and title
    - Format nicely
    """
    pass


def create_histogram(data, bins=10, title="Histogram"):
    """
    Create ASCII histogram from numeric data.
    
    Args:
        data (list): List of numeric values
        bins (int): Number of histogram bins
        title (str): Chart title
    
    TODO: Implement histogram
    - Calculate bin ranges
    - Count values in each bin
    - Create ASCII representation
    - Add labels and title
    """
    pass


# Utility Functions
def validate_numeric_column(data_column):
    """
    Validate that a column contains numeric data.
    
    Args:
        data_column (list): Column data to validate
    
    Returns:
        tuple: (is_valid, cleaned_data)
    
    TODO: Implement validation
    - Check for numeric values
    - Handle string numbers
    - Remove non-numeric values
    - Return validation result and cleaned data
    """
    pass


def get_column_from_dataset(dataset, column_name):
    """
    Extract a specific column from dataset.
    
    Args:
        dataset (list): List of dictionaries
        column_name (str): Name of column to extract
    
    Returns:
        list: Column values
    
    TODO: Implement column extraction
    - Extract values for specified column
    - Handle missing keys
    - Return as list
    """
    pass


def save_results_to_file(results, filename):
    """
    Save analysis results to file.
    
    Args:
        results (dict): Results to save
        filename (str): Output filename
    
    TODO: Implement file saving
    - Convert results to JSON
    - Save to file
    - Handle file errors
    - Confirm save operation
    """
    pass


if __name__ == "__main__":
    main()

# Example dataset structure:
# datasets = {
#     "Sales Data": [
#         {"date": "2024-01-01", "product": "Widget A", "sales": 100, "region": "North"},
#         {"date": "2024-01-02", "product": "Widget B", "sales": 150, "region": "South"},
#         # ... more records
#     ]
# }

# Example analysis results structure:
# analysis_results = [
#     {
#         "timestamp": "2024-01-15T10:30:00",
#         "dataset": "Sales Data",
#         "analysis_type": "descriptive_stats",
#         "column": "sales",
#         "results": {
#             "mean": 125.5,
#             "median": 120.0,
#             "std_dev": 25.3,
#             "min": 75,
#             "max": 200
#         }
#     }
# ]

# Expected behavior:
# The tool should provide a complete data analysis workflow:
# 1. Load/create datasets (using lists and dictionaries)
# 2. Clean data (using sets for deduplication)
# 3. Analyze data (statistical functions)
# 4. Visualize results (text-based charts)
# 5. Generate reports (formatted output)
# 6. Export results (to various formats)
#
# This integrates all data structures learned in Week 4 into a practical,
# real-world application that students can use for actual data analysis tasks.
