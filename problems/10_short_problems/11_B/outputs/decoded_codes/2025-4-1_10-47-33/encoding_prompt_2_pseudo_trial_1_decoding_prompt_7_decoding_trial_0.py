# Step 1: Start of the code

# Step 2: Read an integer value from the user and take its absolute value.
targetNumber = abs(int(input()))

# Step 3: Initialize the current index to 0.
currentIndex = 0

# Step 4: Enter an infinite loop to find the suitable currentIndex.
while True:
    # Calculate the sum of the first currentIndex natural numbers.
    currentSum = (currentIndex * (currentIndex + 1)) // 2
    
    # Determine the difference between currentSum and targetNumber.
    difference = currentSum - targetNumber
    
    # Check if currentSum equals the targetNumber.
    if currentSum == targetNumber:
        print(currentIndex)  # Display currentIndex as the result.
        break  # Exit the loop.
    
    # Check if currentSum is greater than targetNumber.
    elif currentSum > targetNumber:
        # Check if difference is an even number.
        if difference % 2 == 0:
            print(currentIndex)  # Display currentIndex as the result.
            break  # Exit the loop.
    
    # Increment currentIndex by 1 for the next iteration.
    currentIndex += 1

# Step 5: End of the code
