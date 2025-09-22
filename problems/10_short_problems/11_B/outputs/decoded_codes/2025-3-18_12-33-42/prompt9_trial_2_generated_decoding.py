# Get User Input
targetValue = int(input())  # Convert input to a positive integer

# Initialize Variables
index = 0  # This will be used to track the current triangular number being evaluated

# Infinite Loop
while True:
    # Calculate Triangular Number
    triangularNumber = (index * (index + 1)) // 2  # Use integer division for exact result
    
    # Calculate Difference
    difference = triangularNumber - targetValue
    
    # Check for Exact Match
    if triangularNumber == targetValue:
        print(index)  # Print the value of index
        break  # Exit the loop
        
    # Check for Greater Value
    if triangularNumber > targetValue:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the value of index
            break  # Exit the loop
    
    # Increment Index
    index += 1  # Increase index by 1
