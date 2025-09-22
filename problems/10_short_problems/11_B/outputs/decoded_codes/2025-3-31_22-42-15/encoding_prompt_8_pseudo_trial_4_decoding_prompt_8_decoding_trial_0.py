# Get Input
targetNumber = abs(int(input()))

# Initialize Counter
counter = 0

# Start Infinite Loop
while True:
    # Calculate Sum
    currentSum = (counter * (counter + 1)) // 2

    # Calculate Difference
    difference = currentSum - targetNumber

    # Check for Matching Sum
    if currentSum == targetNumber:
        print(counter)
        break

    # Check for Exceeding Sum
    if currentSum > targetNumber:
        if difference % 2 == 0:
            print(counter)
            break

    # Increment Counter
    counter += 1
