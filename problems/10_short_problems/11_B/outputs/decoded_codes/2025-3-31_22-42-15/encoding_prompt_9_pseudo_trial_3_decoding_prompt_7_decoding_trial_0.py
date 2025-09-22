# Purpose: To find the smallest non-negative integer such that the sum of the first i integers 
# equals or can be made to equal a given non-negative integer by removing an even integer

# Step 1: Get Input
targetSum = abs(int(input()))  # Read a non-negative integer from the user and get its absolute value

# Step 2: Initialize a Counter
currentIndex = 0  # This will help track the current integer we are processing

# Step 3: Loop for Calculation
while True:
    # Calculate the sum of the first currentIndex integers
    currentSum = (currentIndex * (currentIndex + 1)) // 2  # Using integer division for accuracy
    
    # Calculate the difference
    difference = currentSum - targetSum  # Determine how far currentSum is from targetSum
    
    # Check Conditions
    if currentSum == targetSum:
        print(currentIndex)  # If equal to targetSum, print currentIndex and stop
        break  # Exit the loop
    elif currentSum > targetSum:
        if difference % 2 == 0:  # Check if the difference is even
            print(currentIndex)  # If difference is even, print currentIndex and stop
            break  # Exit the loop
    
    # Increment currentIndex to check the next integer
    currentIndex += 1  # Move to the next integer
