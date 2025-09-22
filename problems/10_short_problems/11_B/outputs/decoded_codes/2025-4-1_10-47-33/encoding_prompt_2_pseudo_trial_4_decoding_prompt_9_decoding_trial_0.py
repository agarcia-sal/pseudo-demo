# Start

# Read an integer from the user and store the absolute value in targetSum
targetSum = abs(int(input()))

# Initialize currentIndex to 0
currentIndex = 0

# Loop: Begin an infinite loop that continues until explicitly broken
while True:
    # Calculate sum of the first currentIndex integers
    currentSum = (currentIndex * (currentIndex + 1)) // 2
    
    # Calculate the difference from target
    differenceFromTarget = currentSum - targetSum
    
    # Check for exact match
    if currentSum == targetSum:
        print(currentIndex)  # Output the value of currentIndex
        break  # Exit the loop

    # Check for exceeding target
    if currentSum > targetSum:
        # Check if the differenceFromTarget is even
        if differenceFromTarget % 2 == 0:
            print(currentIndex)  # Output the value of currentIndex
            break  # Exit the loop

    # Increment currentIndex
    currentIndex += 1

# End
