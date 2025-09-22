# Start
targetSum = abs(int(input()))
index = 0

# Loop
while True:
    # Calculate
    currentSum = index * (index + 1) // 2
    # Calculate Difference
    difference = currentSum - targetSum
    
    # Check for Exact Match
    if currentSum == targetSum:
        # Output
        print(index)
        # Terminate Loop
        break

    # Check for Overshoot
    if currentSum > targetSum:
        # Check Parity
        if difference % 2 == 0:
            # Output
            print(index)
            # Terminate Loop
            break
    
    # Increment
    index += 1
# End
