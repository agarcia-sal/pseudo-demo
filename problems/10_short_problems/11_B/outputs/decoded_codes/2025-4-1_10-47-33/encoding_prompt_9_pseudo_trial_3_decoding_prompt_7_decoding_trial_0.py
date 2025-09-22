# Purpose: Determine the smallest non-negative integer such that the sum of integers 
# from 0 to that integer either equals a given target number or exceeds it by an even amount.

# Step 1: Receive Input
targetValue = abs(int(input()))  # Convert input to absolute integer

# Step 2: Initialize Variables
index = 0  # Counter to track the current integer

# Step 3: Infinite Loop
while True:
    # Step 3.1: Calculate Sum
    currentSum = (index * (index + 1)) // 2  # Calculate the sum of integers from 0 to index

    # Step 3.2: Calculate Difference
    diff = currentSum - targetValue  # Compute the difference from the target value

    # Step 3.3: Check for Equality
    if currentSum == targetValue:
        print(index)  # Output the current index
        break  # Exit the loop

    # Step 3.4: Check for Greater Sum
    if currentSum > targetValue:
        if diff % 2 == 0:  # Check if the difference is even
            print(index)  # Output the current index
            break  # Exit the loop

    # Step 3.5: Increment Index
    index += 1  # Increase the index for the next iteration
