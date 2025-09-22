# Start
# Read an integer value from the user and take its absolute value. Store this in targetNumber.
targetNumber = abs(int(input()))

# Initialize currentIndex to 0.
currentIndex = 0

# Enter an infinite loop.
while True:
    # Calculate the sum of the first currentIndex natural numbers and store it in currentSum.
    currentSum = currentIndex * (currentIndex + 1) // 2  # This is the formula for the sum of the first n natural numbers

    # Determine the difference between currentSum and targetNumber.
    difference = currentSum - targetNumber

    # If currentSum is equal to targetNumber:
    if currentSum == targetNumber:
        # Display currentIndex as the result.
        print(currentIndex)
        # Exit the loop.
        break
    # Else if currentSum is greater than targetNumber:
    elif currentSum > targetNumber:
        # Check if difference is an even number:
        if difference % 2 == 0:
            # If it is even, display currentIndex as the result.
            print(currentIndex)
            # Exit the loop.
            break

    # Increment currentIndex by 1.
    currentIndex += 1
# End
