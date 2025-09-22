# Receive Input
targetValue = abs(int(input()))  # Read input and convert it to an absolute integer

# Initialize Variables
index = 0  # Counter to keep track of the current integer

# Infinite Loop
while True:
    # Calculate Sum
    currentSum = (index * (index + 1)) // 2  # Use integer division for sum calculation
    
    # Calculate Difference
    diff = currentSum - targetValue  # Compute the difference

    # Check for Equality
    if currentSum == targetValue:
        print(index)  # Output the current integer
        break  # Exit the loop

    # Check for Greater Sum
    if currentSum > targetValue:
        if diff % 2 == 0:  # Check if the difference is even
            print(index)  # Output the current integer
            break  # Exit the loop

    # Increment Index
    index += 1  # Increase the value of index by 1
