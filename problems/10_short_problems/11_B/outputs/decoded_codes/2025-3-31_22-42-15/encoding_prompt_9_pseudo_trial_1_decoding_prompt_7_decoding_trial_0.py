# Purpose: Find the least non-negative integer whose triangular number is equal to or exceeds 
# a given positive integer and outputs that integer if the difference is even.

# Initialize Variables
absoluteValue = abs(int(input()))  # Read input as an integer and take absolute value
index = 0  # Initialize index for triangular number calculation

# Start an Infinite Loop to calculate triangular numbers
while True:
    # Calculate Triangular Number using the formula
    triangularNumber = (index * (index + 1)) // 2
    
    # Calculate the Difference
    difference = triangularNumber - absoluteValue
    
    # Check for Equality
    if triangularNumber == absoluteValue:
        print(index)  # Output index when the triangular number equals absolute value
        break  # Exit the loop
    
    # Check for Greater Value
    if triangularNumber > absoluteValue:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Output index if the difference is even
            break  # Exit the loop
    
    # Increment Index for the next iteration
    index += 1
