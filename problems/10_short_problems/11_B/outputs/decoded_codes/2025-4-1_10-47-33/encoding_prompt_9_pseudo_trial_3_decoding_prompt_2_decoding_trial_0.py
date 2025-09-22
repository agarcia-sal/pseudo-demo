# Step 1: Receive Input
targetValue = abs(int(input()))

# Step 2: Initialize Variables
index = 0

# Step 3: Infinite Loop
while True:
    # Step 3.1: Calculate Sum
    currentSum = (index * (index + 1)) // 2  # Use integer division

    # Step 3.2: Calculate Difference
    diff = currentSum - targetValue

    # Step 3.3: Check for Equality
    if currentSum == targetValue:
        print(index)  # Output the current index
        break  # Exit the loop

    # Step 3.4: Check for Greater Sum
    if currentSum > targetValue:
        if diff % 2 == 0:  # Check if diff is even
            print(index)  # Output the current index
            break  # Exit the loop

    # Step 3.5: Increment Index
    index += 1
