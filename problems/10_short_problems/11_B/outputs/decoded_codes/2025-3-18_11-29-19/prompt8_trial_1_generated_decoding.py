# Initialize Input
targetSum = abs(int(input()))

# Initialize Variables
currentIndex = 0

# Repeat Until Found
while True:
    # Calculate currentSum as the sum of the first currentIndex integers
    currentSum = (currentIndex * (currentIndex + 1)) // 2
    
    # Calculate the difference
    difference = currentSum - targetSum

    # Check Conditions
    if currentSum == targetSum:
        print(currentIndex)  # Solution found
        break
    if currentSum > targetSum:
        if difference % 2 == 0:  # Check if difference is even
            print(currentIndex)  # Solution found
            break
    
    # Increment currentIndex by 1
    currentIndex += 1
