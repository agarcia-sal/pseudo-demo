# Get Input
targetSum = abs(int(input()))

# Initialize a Counter
currentIndex = 0

# Loop for Calculation
while True:
    # Calculate the sum of the first currentIndex integers
    currentSum = (currentIndex * (currentIndex + 1)) // 2

    # Calculate the difference
    difference = currentSum - targetSum
    
    # Check Conditions
    if currentSum == targetSum:
        print(currentIndex)
        break
    if currentSum > targetSum:
        if difference % 2 == 0:
            print(currentIndex)
            break

    # Increment currentIndex by 1
    currentIndex += 1
