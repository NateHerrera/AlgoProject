"""
Project 1:  Convex Hull
Course:     CS 3343-004
Author:     Joey Barrientes - zcj245
Author:     NathanielHerrera - jml045
Date:       March 6, 2025
"""

## Convex Hull
baseCasePoints: int = 3

def convexHull(points):
    # Base case: If there are 3 points or less,
    # return them as the convex hull
    if len(points) <= baseCasePoints:
        return points
    
    # Step 1: Divide

    # Step 2: Recursively compute convex hulls

    # Step 3: Merge
    # return null
    return mergeHulls(leftHull, rightHull)

def mergeHulls(leftHull, rightHull):
    # Step 1: Find upper tangent

    # Step 2: Find lower tangent

    # Step 3: Combine hulls

    # Step 4: Return merged hull
    return null


## Main
inputFilename: str = "input.csv"
outputFilename: str = "output.txt"

# Read input from file
def readInput(filename):
    points: list = []
    with open(filename) as file:
        for line in file:
            x, y = line.split(',')
            points.append((float(x), float(y)))
    return points

points = readInput(inputFilename)
print(points)
    
# Compute convex hull
    
# Write output to file