# Step 1: Obtain a positive integer input and store its absolute value
targetValue = abs(int(input()))

# Step 2: Initialize a counter variable
currentIndex = 0

# Step 3: Enter an infinite loop
while True:
    # Compute the sum of the first `currentIndex` natural numbers
    currentSum = currentIndex * (currentIndex + 1) // 2
    
    # Determine the difference between `currentSum` and `targetValue`
    difference = currentSum - targetValue
    
    # Step 4: Check if `currentSum` is equal to `targetValue`
    if currentSum == targetValue:
        print(currentIndex)  # Output the value of `currentIndex`
        break  # Exit the loop
    
    # Step 5: If `currentSum` is greater than `targetValue`
    if currentSum > targetValue:
        # Check if `difference` is an even number
        if difference % 2 == 0:
            print(currentIndex)  # Output the value of `currentIndex`
            break  # Exit the loop
    
    # Step 6: Increment `currentIndex` by 1
    currentIndex += 1

# Step 7: End the process (implicitly done by exiting the loop)
