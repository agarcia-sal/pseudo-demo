# Get and Prepare Input
targetSum = abs(int(input()))

# Initialize Counter
index = 0

# Start Infinite Loop
while True:
    # Calculate Triangular Number
    triangularNumber = (index * (index + 1)) // 2
    
    # Calculate Difference
    difference = triangularNumber - targetSum
    
    # Check for Equality
    if triangularNumber == targetSum:
        print(index)
        break
    
    # Check for Overreach
    elif triangularNumber > targetSum:
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment Counter
    index += 1
