# Start of the program

# Step 1: Read an integer from the user and take its absolute value
targetSum = abs(int(input()))

# Step 2: Initialize index to zero
index = 0

# Step 3: Begin an infinite loop
while True:
    # Step 4: Calculate the sum of the first 'index' natural numbers
    currentSum = index * (index + 1) // 2  # Use integer division for accuracy

    # Step 5: Calculate the difference
    difference = currentSum - targetSum
    
    # Step 6: Check for exact match
    if currentSum == targetSum:
        print(index)  # Output the value of index
        break  # Terminate the loop
    
    # Step 7: Check for overshoot
    if currentSum > targetSum:
        # Step 8: Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the value of index
            break  # Terminate the loop

    # Step 9: Increment the index
    index += 1

# End of the program
