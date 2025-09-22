# Start: Begin the algorithm.

# Input: Read an integer value from the user
targetValue = abs(int(input()))

# Initialize: Set a counter variable
currentIndex = 0 

# Loop: Continue executing the following steps indefinitely
while True:
    # Calculate Sum
    currentSum = (currentIndex * (currentIndex + 1)) / 2

    # Calculate Difference
    differenceFromTarget = currentSum - targetValue

    # Check Conditions
    if currentSum == targetValue:
        # Output: Print currentIndex as it is the solution
        print(currentIndex)
        # Exit: Terminate the loop
        break
    elif currentSum > targetValue:
        if differenceFromTarget % 2 == 0:  # Check if the difference is even
            # Output: Print currentIndex as it is the solution
            print(currentIndex)
            # Exit: Terminate the loop
            break

    # Increment: Increase currentIndex by 1
    currentIndex += 1

# End: Conclude the algorithm once a result has been printed and the loop is exited.
