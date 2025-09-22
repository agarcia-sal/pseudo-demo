# Step 1: Receive input
# Get the input number and take its absolute value
targetValue = abs(int(input()))

# Step 2: Initialize a counter
counter = 0

# Step 3: Begin an infinite loop
while True:
    # Step 4: Calculate the sum of integers
    currentSum = counter * (counter + 1) // 2  # Using integer division

    # Step 5: Calculate the difference
    difference = currentSum - targetValue

    # Step 6: Check equality
    if currentSum == targetValue:
        print(counter)  # Output the result
        break  # End the loop

    # Step 7: Check exceedance condition
    if currentSum > targetValue:
        if difference % 2 == 0:  # Check if the difference is even
            print(counter)  # Output the result
            break  # End the loop

    # Step 8: Increment counter
    counter += 1  # Move to the next integer
