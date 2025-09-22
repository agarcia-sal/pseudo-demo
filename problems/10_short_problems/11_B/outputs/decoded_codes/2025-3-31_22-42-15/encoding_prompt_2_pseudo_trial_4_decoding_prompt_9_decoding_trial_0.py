# Start the program

# Step 2: Input the integer value and take its absolute value
targetNumber = abs(int(input()))

# Step 3: Initialize index
index = 0

# Step 4: Loop indefinitely
while True:
    # Calculate the currentSum using the formula for the sum of the first 'index' natural numbers
    currentSum = (index * (index + 1)) // 2
    
    # Calculate the difference
    difference = currentSum - targetNumber
    
    # Step 5: Conditions
    if currentSum == targetNumber:
        # Case where currentSum is equal to targetNumber
        print(index)
        break  # Exit the loop
    elif currentSum > targetNumber:
        # Case where currentSum is greater than targetNumber
        if difference % 2 == 0:  # Check if the difference is even
            print(index)
            break  # Exit the loop
    
    # Step 6: Update the index for the next iteration
    index += 1

# End of program
