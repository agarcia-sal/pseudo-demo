# Start

# Step 2: Input
targetSum = abs(int(input()))

# Step 3: Initialize
currentIndex = 0

# Step 4: Loop
while True:
    # Step 4.1: Calculate
    currentSum = (currentIndex * (currentIndex + 1)) // 2
    
    # Step 4.2: Calculate Difference
    differenceFromTarget = currentSum - targetSum
    
    # Step 4.3: Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)  # Output the value of currentIndex
        break  # Exit the loop
    
    # Step 4.4: Check for Exceeding Target
    if currentSum > targetSum:
        if differenceFromTarget % 2 == 0:  # Check if even
            print(currentIndex)  # Output the value of currentIndex
            break  # Exit the loop
    
    # Step 4.5: Increment
    currentIndex += 1

# End of Loop

# End
