# Step 1: Get Input
targetNumber = abs(int(input()))

# Step 2: Initialize Counter
counter = 0

# Step 3: Start Infinite Loop
while True:
    # Step 3a: Calculate Sum
    currentSum = (counter * (counter + 1)) // 2  # Use integer division

    # Step 3b: Calculate Difference
    difference = currentSum - targetNumber

    # Step 3c: Check for Matching Sum
    if currentSum == targetNumber:
        print(counter)  # Print the value of counter
        break  # Exit the loop

    # Step 3d: Check for Exceeding Sum
    if currentSum > targetNumber:
        if difference % 2 == 0:  # Check if difference is even
            print(counter)  # Print the value of counter
            break  # Exit the loop

    # Step 3e: Increment Counter
    counter += 1  # Increase the value of counter by 1
