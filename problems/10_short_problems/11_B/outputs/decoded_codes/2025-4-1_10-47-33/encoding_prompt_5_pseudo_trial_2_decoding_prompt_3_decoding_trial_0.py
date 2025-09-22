# This program finds a non-negative integer i such that the sum of the first i integers
# either equals a given non-negative integer n or the difference between this sum and n is even.

def find_integer_for_sum():
    # Step 2: Input the Number
    targetSum = abs(int(input()))  # Read input and take the absolute integer

    # Step 3: Initialize Counter
    index = 0

    # Step 4: Begin Infinite Loop
    while True:
        # Step 4a: Calculate the Sum of the First 'index' Integers
        currentSum = (index * (index + 1)) // 2  # Use integer division

        # Step 4b: Calculate the Difference
        difference = currentSum - targetSum

        # Step 4c: Check for Equality
        if currentSum == targetSum:
            print(index)  # Found exact match
            break
        
        # Step 4d: Check for Exceeding the Target
        if currentSum > targetSum:
            if difference % 2 == 0:  # Check if the difference is even
                print(index)  # Valid result found
                break
        
        # Step 4e: Increment the Counter
        index += 1

# Start the program by calling the function
find_integer_for_sum()
