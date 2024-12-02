#!/usr/bin/python3
"""
Function to calculate the perimeter of the island described in the grid.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.
    
    Args:
    grid (list of list of ints): 2D grid representing the map of the island.
    
    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is land
            if grid[i][j] == 1:
                # Check all four possible directions (up, down, left, right)
                
                # Top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                
                # Bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                
                # Left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                
                # Right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                
    return perimeter
