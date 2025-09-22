# Step 1: Receive input
targetValue = abs(int(input()))

# Step 2: Initialize a counter
counter = 0

# Step 3: Begin an infinite loop
while True:
    # Step 4: Calculate the sum of integers
    currentSum = counter * (counter + 1) // 2  # Use // for integer division

    # Step 5: Calculate the difference
    difference = currentSum - targetValue

    # Step 6: Check equality
    if currentSum == targetValue:
        print(counter)  # Output counter as the solution
        break  # End the loop

    # Step 7: Check exceedance condition
    if currentSum > targetValue:
        if difference % 2 == 0:  # Check if difference is even
            print(counter)  # Output counter as the solution
            break  # End the loop

    # Step 8: Increment counter
    counter += 1

# Step 9: End of pseudocode (implicitly ends here)
