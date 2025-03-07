"""
Project 1: Convex Hull
Course: CS 3343-004
Author: Joey Barrientes - zcj245
Author: Nathaniel Herrera - jml045
Date: March 6, 2025
"""

from functools import cmp_to_key

# Calculates the orientation of the angle formed by three points
def calculateAngleOrientation(a, b, c):
    crossProduct = (b[1] - a[1]) * (c[0] - b[0]) - (c[1] - b[1]) * (b[0] - a[0])
    if crossProduct > 0: # Counter-clockwise
        return 1
    if crossProduct < 0: # Clockwise
        return -1

# Compares two points relative to a midpoint for sorting purposes.
def pointCompare(midCentroid, point1, point2):
    p = [point1[0] - midCentroid[0], point1[1] - midCentroid[1]]
    q = [point2[0] - midCentroid[0], point2[1] - midCentroid[1]]
	
	# Compare using cross product
    return -1 if p[1] * q[0] < q[1] * p[0] else 1

# Merges two convex hulls into one.
def mergeHulls(leftHull, rightHull):
    leftLength = len(leftHull)
    rightLength = len(rightHull)

    # Step 1: Find the rightmost point of the left hull and the leftmost point of the right hull
    rightmostLeft = max(range(leftLength), key=lambda i: leftHull[i][0])
    leftmostRight = min(range(rightLength), key=lambda i: rightHull[i][0])

    upperLeft = rightmostLeft
    upperRight = leftmostRight

    # Step 2: Find the upper tangent
    while True:
        # Move the upper left point clockwise if necessary
        while calculateAngleOrientation(rightHull[upperRight], leftHull[upperLeft], leftHull[(upperLeft + 1) % leftLength]) >= 0:
            upperLeft = (upperLeft + 1) % leftLength
        # Move the upper right point counterclockwise if necessary
        while calculateAngleOrientation(leftHull[upperLeft], rightHull[upperRight], rightHull[(upperRight - 1) % rightLength]) <= 0:
            upperRight = (upperRight - 1) % rightLength
            break  # Break to recheck after updating `upperRight`
        else:
            break  # Break when no changes were made in the previous loop

    # Step 3: Find the lower tangent
    nextUpperLeft = upperLeft
    nextUpperRight = upperRight
    upperLeft = rightmostLeft
    upperRight = leftmostRight
    while True:
        # Move the lower left point counterclockwise if necessary
        while calculateAngleOrientation(leftHull[upperLeft], rightHull[upperRight], rightHull[(upperRight + 1) % rightLength]) >= 0:
            upperRight = (upperRight + 1) % rightLength
        # Move the lower right point clockwise if necessary
        while calculateAngleOrientation(rightHull[upperRight], leftHull[upperLeft], leftHull[(upperLeft - 1) % leftLength]) <= 0:
            upperLeft = (upperLeft - 1) % leftLength
            break  # Break to recheck after updating `upperLeft`
        else:
            break  # Break when no changes were made in the previous loop

    nextLowerLeft = upperLeft
    nextLowerRight = upperRight
    result = []

    # Collect the points from the left hull
    index = nextUpperLeft
    result.append(leftHull[nextUpperLeft])
    while index != nextLowerLeft:
        index = (index + 1) % leftLength
        result.append(leftHull[index])

    # Collect the points from the right hull
    index = nextLowerRight
    result.append(rightHull[nextLowerRight])
    while index != nextUpperRight:
        index = (index + 1) % rightLength
        result.append(rightHull[index])

    return result


# Computes the convex hull for a small set of points (base case)
def computeBaseCasePoints(points):
    s = set()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, x2 = points[i][0], points[j][0]
            y1, y2 = points[i][1], points[j][1]
            a1, b1, c1 = y1 - y2, x2 - x1, x1 * y2 - y1 * x2
            pos, neg = 0, 0
            for k in range(len(points)):
                if (k == i) or (k == j) or (a1 * points[k][0] + b1 * points[k][1] + c1 <= 0):
                    neg += 1
                if (k == i) or (k == j) or (a1 * points[k][0] + b1 * points[k][1] + c1 >= 0):
                    pos += 1
            if pos == len(points) or neg == len(points):
                s.add(tuple(points[i]))
                s.add(tuple(points[j]))

    completedHull = [list(x) for x in s]
    midCentroid = [sum(x[0] for x in completedHull) / len(completedHull), sum(x[1] for x in completedHull) / len(completedHull)]
    completedHull = sorted(completedHull, key=cmp_to_key(lambda p1, p2: pointCompare(midCentroid, p1, p2)))
    return completedHull, midCentroid

# Recursively computes the convex hull for a set of points
def computeConvexHull(points):
    # Base case: 3 or fewer points
    if len(points) <= 3:
        return computeBaseCasePoints(points)[0]

    # Step 1: Divide the points into two sets
    midPoint = len(points) // 2
    leftPoints = points[:midPoint]
    rightPoints = points[midPoint:]

    # Step 2: Recursively compute the convex hull for each set
    leftHull = computeConvexHull(leftPoints)
    rightHull = computeConvexHull(rightPoints)

    # Step 3: Merge the two convex hulls
    return mergeHulls(leftHull, rightHull)

# Reads a list of points from a file
def readInput(filename):
    points = []
    with open(filename) as file:
        for line in file:
            x, y = line.split(',')
            points.append((float(x), float(y)))
    return points

# Compares two points with a tolerance to account for floating-point precision
def comparePoints(point1, point2):
    compareTolerance = 1e-9
    return abs(point1[0] - point2[0]) < compareTolerance and abs(point1[1] - point2[1]) < compareTolerance

# Writes the indices of the convex hull points to a file.
def writeOutput(filename, hullIndices):
    with open(filename, 'w') as file:
        for index in hullIndices:
            file.write(str(index) + '\n')

if __name__ == '__main__':
    inputFilename = "input.csv"
    outputFilename = "output.txt"

    points = readInput(inputFilename)
    completedHull = computeConvexHull(points)

    hullIndices = []
    for point in completedHull:
        for i, p in enumerate(points):
            if comparePoints(point, p):
                hullIndices.append(i)
                break

    writeOutput(outputFilename, hullIndices)
    print("Convex Hull Indices:", hullIndices)
    print("Output written to", outputFilename)
