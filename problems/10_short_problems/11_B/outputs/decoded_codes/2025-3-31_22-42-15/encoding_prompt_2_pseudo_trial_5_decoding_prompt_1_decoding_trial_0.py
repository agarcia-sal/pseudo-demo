# Step 1: Input Requirement
targetSum = abs(int(input()))  # Read an integer value and store its absolute value

# Step 2: Initialize a counter
currentIndex = 0  # Set currentIndex to 0

# Step 3: Loop Until a Condition is Met
while True:  # Begin an infinite loop

    # Step 4: Calculate the Sum
    sumOfSeries = (currentIndex * (currentIndex + 1)) // 2  # Sum of the first currentIndex integers

    # Step 5: Compute Difference
    difference = sumOfSeries - targetSum  # Determine the difference

    # Step 6: Check Conditions
    if sumOfSeries == targetSum:  # Check if the sum equals targetSum
        print(currentIndex)  # Output currentIndex
        break  # Stop the loop
    if sumOfSeries > targetSum:  # Check if sum exceeds targetSum
        if difference % 2 == 0:  # Check if difference is even
            print(currentIndex)  # Output currentIndex
            break  # Stop the loop

    # Step 7: Increment the Counter
    currentIndex += 1  # Increase currentIndex by 1
