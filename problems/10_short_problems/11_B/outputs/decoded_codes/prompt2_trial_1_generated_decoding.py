# Start

# Receive Input
targetNumber = abs(int(input()))

# Initialize Counter
index = 0

# Infinite Loop
while True:
    # Calculate Sum
    currentSum = (index * (index + 1)) / 2
    
    # Calculate Difference
    difference = currentSum - targetNumber
    
    # Check for Exact Match
    if currentSum == targetNumber:
        print(index)  # Output the value of index
        break  # Exit the loop
    
    # Check for Exceeding Target
    if currentSum > targetNumber:
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # Output the value of index
            break  # Exit the loop
    
    # Increment Counter
    index += 1

# End
