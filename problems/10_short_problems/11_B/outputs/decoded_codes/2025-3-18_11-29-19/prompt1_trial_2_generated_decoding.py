# Step 1: Input
targetSum = abs(int(input()))  # Read input and take absolute value

# Step 2: Initialize Variables
index = 0  # Set index to 0

# Step 3: Loop Until Condition is Met
while True:  # Repeat indefinitely
    
    # Step 3a: Calculate Sum
    sumOfIntegers = (index * (index + 1)) / 2  # Compute sum of first index integers
    
    # Step 3b: Calculate Difference
    difference = sumOfIntegers - targetSum  # Determine the difference
    
    # Step 3c: Check for Exact Match
    if sumOfIntegers == targetSum:  # Check if sums are equal
        print(index)  # Output the current value of index
        break  # Exit the loop
    
    # Step 3d: Check for Greater Sum
    if sumOfIntegers > targetSum:  # Check if sum is greater than target
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # Output current value of index
            break  # Exit the loop
    
    # Step 3e: Increment Index
    index += 1  # Increase index by 1
