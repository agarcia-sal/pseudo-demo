# Start of the program

# Step 1: Get Input
targetSum = abs(int(input()))  # Receive a number from the user and take its absolute value

# Step 2: Initialize Counter
currentIndex = 0  # Variable to keep track of the current integer being evaluated

# Step 3: Loop Indefinitely
while True:  # Begin an infinite loop to evaluate consecutive integers
    # Step 3a: Calculate Sum
    currentSum = currentIndex * (currentIndex + 1) // 2  # Calculate sum of integers from 0 to currentIndex
    
    # Step 3b: Difference Calculation
    difference = currentSum - targetSum  # Calculate the difference from the targetSum

    # Step 3c: Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)  # Output the result
        break  # Exit the loop
    
    # Step 3d: Check for Overshoot
    if currentSum > targetSum:
        if difference % 2 == 0:  # If the difference is even
            print(currentIndex)  # Output the result
            break  # Exit the loop

    # Step 3e: Increment Index
    currentIndex += 1  # Increase currentIndex by 1 for the next iteration

# End of the program
