# Step 1: Read an integer value
targetValue = abs(int(input()))

# Step 2: Initialization of index
index = 0

# Step 3: Loop to find the smallest non-negative integer satisfying the conditions
while True:
    # Step 3a: Calculate the current sum using the formula for the sum of the first 'index' integers
    currentSum = (index * (index + 1)) // 2

    # Step 3b: Calculate the difference between currentSum and targetValue
    difference = currentSum - targetValue

    # Step 3c: Check if currentSum equals targetValue
    if currentSum == targetValue:
        print(index)  # Output the index and stop the loop
        break  # Exit the loop

    # Step 3d: Check if currentSum is greater than targetValue
    if currentSum > targetValue:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index and stop the loop
            break  # Exit the loop

    # Step 3e: Increment index for the next iteration
    index += 1
