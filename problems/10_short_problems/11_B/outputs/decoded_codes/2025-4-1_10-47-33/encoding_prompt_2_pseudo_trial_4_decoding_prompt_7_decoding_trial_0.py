# Start of the program

# Step 2: Input - Read an integer and store its absolute value
targetSum = abs(int(input()))

# Step 3: Initialize currentIndex to 0
currentIndex = 0

# Step 4: Begin an infinite loop
while True:
    # Step 4.1: Calculate currentSum using the formula
    currentSum = (currentIndex * (currentIndex + 1)) // 2  # Use integer division
    
    # Step 4.2: Calculate the difference from targetSum
    differenceFromTarget = currentSum - targetSum
    
    # Step 4.3: Check for an exact match
    if currentSum == targetSum:
        print(currentIndex)  # Output the currentIndex
        break  # Exit the loop
    
    # Step 4.4: Check if currentSum exceeds targetSum
    if currentSum > targetSum:
        # Check if the difference is even
        if differenceFromTarget % 2 == 0:
            print(currentIndex)  # Output the currentIndex
            break  # Exit the loop
    
    # Step 4.5: Increment currentIndex by 1
    currentIndex += 1

# End of the program
