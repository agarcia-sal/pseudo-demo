# Step 1: Start
# Step 2: Read an integer value from the user and take its absolute value.
targetNumber = abs(int(input()))

# Step 3: Initialize a variable currentIndex to 0.
currentIndex = 0

# Step 4: Enter an infinite loop.
while True:
    # Calculate the sum of the first currentIndex natural numbers.
    currentSum = currentIndex * (currentIndex + 1) // 2  # This uses the formula n(n+1)/2 for sum of first n natural numbers.
    
    # Determine the difference between currentSum and targetNumber.
    difference = currentSum - targetNumber
    
    # If currentSum is equal to targetNumber:
    if currentSum == targetNumber:
        print(currentIndex)  # Display currentIndex as the result.
        break  # Exit the loop.
    
    # Else if currentSum is greater than targetNumber:
    elif currentSum > targetNumber:
        # Check if difference is an even number:
        if difference % 2 == 0:
            print(currentIndex)  # Display currentIndex as the result.
            break  # Exit the loop.
    
    # Increment currentIndex by 1.
    currentIndex += 1

# Step 5: End (implicit as code execution ends here)
