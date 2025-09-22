# Step 1: Get Input
targetSum = abs(int(input()))  # Receive a number and calculate its absolute value

# Step 2: Initialize Counter
currentIndex = 0  # This will track the current integer being evaluated

# Step 3: Loop Indefinitely
while True:  # Start an infinite loop to evaluate consecutive integers

    # Step 3a: Calculate Sum
    currentSum = currentIndex * (currentIndex + 1) // 2  # Calculate sum from 0 to currentIndex

    # Step 3b: Difference Calculation
    difference = currentSum - targetSum  # Calculate difference from targetSum

    # Step 3c: Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)  # Output currentIndex and terminate the loop
        break

    # Step 3d: Check for Overshoot
    if currentSum > targetSum:
        if difference % 2 == 0:  # Check if the difference is even
            print(currentIndex)  # Output currentIndex and terminate the loop
            break

    # Step 3e: Increment Index
    currentIndex += 1  # Increment currentIndex for the next loop iteration
