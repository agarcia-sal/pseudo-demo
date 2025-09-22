# Purpose: Find a non-negative integer i such that 
# the sum of the first i integers equals a given non-negative integer n 
# or the difference between this sum and n is an even number.

# Start Program

# Step 2: Input the Number
targetSum = abs(int(input()))  # Read user input and convert to absolute integer

# Step 3: Initialize Counter
index = 0  # Set a counter variable

# Step 4: Begin Infinite Loop
while True:  # Repeat indefinitely

    # Step 4a: Calculate the Sum of the First 'index' Integers
    currentSum = (index * (index + 1)) // 2  # Using integer division to avoid float results

    # Step 4b: Calculate the Difference
    difference = currentSum - targetSum  # Determine the difference

    # Step 4c: Check for Equality
    if currentSum == targetSum:
        print(index)  # Print the result if sums match
        break  # Exit the loop

    # Step 4d: Check for Exceeding the Target
    if currentSum > targetSum:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the result if difference is even
            break  # Exit the loop

    # Step 4e: Increment the Counter
    index += 1  # Increase the value of index by 1

# End Program
