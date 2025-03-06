"""
Project 1:  Convex Hull
Course:     CS 3343-004
Author:     Joey Barrientes - zcj245
Author:     NathanielHerrera - jml045
Date:       March 6, 2025
"""
import math
## Convex Hull
baseCasePoints: int = 3

def convexHull(points):
    # Base case: If there are 3 points or less,
    # return them as the convex hull
    if len(points) <= baseCasePoints:
        return points
    
    # Step 1: Divide
    # Split points into left and right halves
    leftPoints = points[:len(points)//2]
    rightPoints = points[len(points)//2:]
    # print("Left points: ", leftPoints, "\n")
    # print("Right points: ", rightPoints, "\n")

    # Step 2: Recursively compute convex hulls
    leftHull = convexHull(leftPoints)
    rightHull = convexHull(rightPoints)
    # print("Left hull: ", leftHull, "\n")
    # print("Right hull: ", rightHull, "\n")

    # Step 3: Merge hulls
    return None
    # return mergeHulls(leftHull, rightHull)

def mergeHulls(leftHull, rightHull):
    # Step 1: Find upper tangent

    # Step 2: Find lower tangent

    # Step 3: Combine hulls 
    
    # Step 4: Return merged hull
    return None
    # return mergedHull


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
    file.close()
    return points

points = readInput(inputFilename)
print("Input points: ", points, "\n")

# Compute convex hull
hull = convexHull(points)
# print(hull)