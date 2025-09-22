# Importing the absolute value function from the math library (if needed)
# but using built-in abs() function directly for simplicity
# from math import abs  

# Step 1: Read an integer input and store its absolute value in targetSum
targetSum = abs(int(input()))

# Step 2: Initialize a counter to track the current index
currentIndex = 0

# Step 3: Begin an infinite loop
while True:
    # Step 4: Calculate the sum of the first 'currentIndex' integers
    sumOfSeries = currentIndex * (currentIndex + 1) // 2  # Using the formula n(n + 1)/2
    
    # Step 5: Compute the difference between sumOfSeries and targetSum
    difference = sumOfSeries - targetSum
    
    # Step 6: Check if the sum matches the targetSum
    if sumOfSeries == targetSum:
        print(currentIndex)  # Output the current index
        break  # Stop the loop
    elif sumOfSeries > targetSum:
        # Step 6: Check if the difference is even
        if difference % 2 == 0:
            print(currentIndex)  # Output the current index
            break  # Stop the loop
    
    # Step 7: Increment the counter to check the next index
    currentIndex += 1
