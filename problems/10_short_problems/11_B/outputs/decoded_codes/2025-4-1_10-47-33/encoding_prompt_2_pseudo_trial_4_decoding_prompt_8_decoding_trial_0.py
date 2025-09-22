# Start

# Input: Read an integer from the user and store the absolute value in a variable named targetSum
targetSum = abs(int(input()))

# Initialize: Set a variable currentIndex to 0
currentIndex = 0

# Loop: Begin an infinite loop that will continue until explicitly broken
while True:
    # Calculate: Determine the sum of the first currentIndex integers
    currentSum = (currentIndex * (currentIndex + 1)) // 2

    # Calculate Difference: Find the difference between currentSum and targetSum
    differenceFromTarget = currentSum - targetSum

    # Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)
        break

    # Check for Exceeding Target
    if currentSum > targetSum:
        if differenceFromTarget % 2 == 0:
            print(currentIndex)
            break

    # Increment: Increase currentIndex by 1
    currentIndex += 1

# End
