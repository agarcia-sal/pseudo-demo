# Get Input Value
targetValue = abs(int(input()))

# Initialize Variables
currentIndex = 0

# Start Infinite Loop
while True:
    # Calculate Sum
    currentSum = (currentIndex * (currentIndex + 1)) // 2

    # Calculate Difference
    difference = currentSum - targetValue

    # Check Conditions
    if currentSum == targetValue:
        print(currentIndex)
        break
    elif currentSum > targetValue:
        if difference % 2 == 0:
            print(currentIndex)
            break

    # Increment Index
    currentIndex += 1
