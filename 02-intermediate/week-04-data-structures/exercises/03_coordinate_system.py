"""
Week 4 - Exercise 3: Coordinate System
Learn tuples and immutability through a coordinate geometry system.

Learning Goals:
- Understand tuple creation and immutability
- Practice tuple unpacking
- Work with nested tuples
- Implement mathematical operations with tuples
- Learn when to use tuples vs lists

Tasks:
1. Create a coordinate system using tuples
2. Calculate distances between points
3. Find geometric properties (midpoint, area, etc.)
4. Store and analyze multiple coordinate sets
5. Implement coordinate transformations
"""

import math


def main():
    """
    Coordinate System Manager
    
    Create a system that works with 2D and 3D coordinates using tuples.
    Demonstrates tuple immutability, unpacking, and mathematical operations.
    
    Requirements:
    - Store coordinates as tuples
    - Calculate distances and midpoints
    - Work with shapes (triangles, rectangles)
    - Transform coordinates (rotation, translation)
    - Analyze coordinate sets
    """
    coordinates = []
    shapes = []
    
    print("📐 Coordinate System Manager")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Add coordinate point")
        print("2. View all points")
        print("3. Calculate distance between points")
        print("4. Find midpoint")
        print("5. Create shape")
        print("6. Analyze shape")
        print("7. Transform coordinates")
        print("8. Exit")
        
        choice = input("\nSelect option (1-8): ").strip()
        
        if choice == "1":
            # TODO: Implement add_coordinate function
            pass
            
        elif choice == "2":
            # TODO: Implement view_coordinates function
            pass
            
        elif choice == "3":
            # TODO: Implement calculate_distance function
            pass
            
        elif choice == "4":
            # TODO: Implement find_midpoint function
            pass
            
        elif choice == "5":
            # TODO: Implement create_shape function
            pass
            
        elif choice == "6":
            # TODO: Implement analyze_shape function
            pass
            
        elif choice == "7":
            # TODO: Implement transform_coordinates function
            pass
            
        elif choice == "8":
            print("Goodbye! 📐")
            break
            
        else:
            print("Invalid option. Please try again.")


def add_coordinate(coordinates):
    """
    Add a coordinate point (2D or 3D) to the list.
    
    Args:
        coordinates (list): List of coordinate tuples
    
    TODO: Implement this function
    - Ask for 2D (x, y) or 3D (x, y, z) coordinate
    - Create tuple from input
    - Add to coordinates list with label
    - Handle invalid input
    """
    pass


def view_coordinates(coordinates):
    """
    Display all coordinate points.
    
    Args:
        coordinates (list): List of coordinate tuples
    
    TODO: Implement this function
    - Display all points with labels
    - Show 2D and 3D points separately
    - Plot points on a simple text grid (for 2D)
    - Show coordinate statistics (range, center)
    """
    pass


def calculate_distance(coordinates):
    """
    Calculate distance between two points.
    
    Args:
        coordinates (list): List of coordinate tuples
    
    TODO: Implement this function
    - Show available points
    - Let user select two points
    - Calculate Euclidean distance
    - Handle both 2D and 3D distances
    - Display result with formula used
    """
    pass


def find_midpoint(coordinates):
    """
    Find midpoint between two coordinates.
    
    Args:
        coordinates (list): List of coordinate tuples
    
    TODO: Implement this function
    - Select two points
    - Calculate midpoint coordinates
    - Return as new tuple
    - Handle 2D and 3D cases
    - Option to add midpoint to coordinates list
    """
    pass


def create_shape(coordinates, shapes):
    """
    Create a geometric shape from existing coordinates.
    
    Args:
        coordinates (list): List of coordinate tuples
        shapes (list): List of created shapes
    
    TODO: Implement this function
    - Create triangles (3 points)
    - Create rectangles (4 points)
    - Create polygons (n points)
    - Store shape as tuple of coordinate tuples
    - Validate shape requirements
    """
    pass


def analyze_shape(shapes):
    """
    Analyze properties of created shapes.
    
    Args:
        shapes (list): List of shape tuples
    
    TODO: Implement this function
    - Calculate area for different shapes
    - Calculate perimeter
    - Find center point
    - Determine if shape is regular
    - Show all properties in formatted output
    """
    pass


def transform_coordinates(coordinates):
    """
    Apply transformations to coordinates.
    
    Args:
        coordinates (list): List of coordinate tuples
    
    TODO: Implement this function
    - Translation (shift by offset)
    - Scaling (multiply by factor)
    - Rotation (around origin)
    - Reflection (across axes)
    - Create new transformed coordinates
    """
    pass


def distance_2d(point1, point2):
    """
    Calculate distance between two 2D points.
    
    Args:
        point1 (tuple): First point (x, y)
        point2 (tuple): Second point (x, y)
    
    Returns:
        float: Distance between points
    
    TODO: Implement this function
    - Use tuple unpacking
    - Apply distance formula: sqrt((x2-x1)² + (y2-y1)²)
    """
    pass


def distance_3d(point1, point2):
    """
    Calculate distance between two 3D points.
    
    Args:
        point1 (tuple): First point (x, y, z)
        point2 (tuple): Second point (x, y, z)
    
    Returns:
        float: Distance between points
    
    TODO: Implement this function
    - Use tuple unpacking
    - Apply 3D distance formula: sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)
    """
    pass


def midpoint_2d(point1, point2):
    """
    Calculate midpoint between two 2D points.
    
    Args:
        point1 (tuple): First point (x, y)
        point2 (tuple): Second point (x, y)
    
    Returns:
        tuple: Midpoint coordinates
    
    TODO: Implement this function
    - Use tuple unpacking
    - Calculate midpoint: ((x1+x2)/2, (y1+y2)/2)
    - Return as new tuple
    """
    pass


def triangle_area(point1, point2, point3):
    """
    Calculate area of triangle using coordinate geometry.
    
    Args:
        point1, point2, point3 (tuple): Triangle vertices (x, y)
    
    Returns:
        float: Area of triangle
    
    TODO: Implement this function
    - Use shoelace formula: |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2
    - Handle tuple unpacking
    """
    pass


if __name__ == "__main__":
    main()

# Example coordinate structure:
# coordinates = [
#     ("A", (0, 0)),      # 2D point
#     ("B", (3, 4)),      # 2D point  
#     ("C", (1, 2, 3)),   # 3D point
# ]

# Example shape structure:
# shapes = [
#     ("Triangle ABC", ((0, 0), (3, 0), (0, 4))),
#     ("Square DEFG", ((1, 1), (4, 1), (4, 4), (1, 4))),
# ]

# Expected behavior example:
#
# 📐 Coordinate System Manager
# ========================================
# 
# Options:
# 1. Add coordinate point
# 2. View all points
# 3. Calculate distance between points
# 4. Find midpoint
# 5. Create shape
# 6. Analyze shape
# 7. Transform coordinates
# 8. Exit
# 
# Select option (1-8): 1
# Enter point label: A
# Enter coordinate type (2D/3D): 2D
# Enter x coordinate: 0
# Enter y coordinate: 0
# ✅ Added point A(0, 0)
# 
# Select option (1-8): 3
# Available points:
# 1. A(0, 0)
# 2. B(3, 4)
# 
# Select first point (1-2): 1
# Select second point (1-2): 2
# 
# Distance between A(0, 0) and B(3, 4):
# Formula: √((3-0)² + (4-0)²) = √(9 + 16) = √25 = 5.0
# Distance: 5.0 units
