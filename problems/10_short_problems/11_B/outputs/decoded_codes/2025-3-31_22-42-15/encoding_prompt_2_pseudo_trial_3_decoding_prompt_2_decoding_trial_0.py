# Step 1: Input
targetValue = abs(int(input()))
# Step 2: Initialization
index = 0

# Step 3: Loop
while True:
    # a. Calculate the currentSum
    currentSum = (index * (index + 1)) // 2  # Using integer division for the sum
    
    # b. Compute the difference
    difference = currentSum - targetValue
    
    # c. Check if currentSum is equal to targetValue
    if currentSum == targetValue:
        print(index)
        break  # Stop the loop if condition is met
    
    # d. Check if currentSum is greater than targetValue
    if currentSum > targetValue:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)
            break  # Stop the loop if condition is met

    # e. Increment index by 1
    index += 1
