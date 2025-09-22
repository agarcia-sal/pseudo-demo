# Get Input
targetSum = abs(int(input()))

# Initialize Counter
currentIndex = 0

# Loop Indefinitely
while True:
    # Calculate Sum
    currentSum = currentIndex * (currentIndex + 1) // 2  # Using integer division
    
    # Difference Calculation
    difference = currentSum - targetSum
    
    # Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)  # Output the result
        break  # Terminate the loop
    
    # Check for Overshoot
    if currentSum > targetSum:
        if difference % 2 == 0:  # Check if difference is even
            print(currentIndex)  # Output the result
            break  # Terminate the loop
    
    # Increment Index
    currentIndex += 1  # Increase currentIndex by 1 for the next iteration
