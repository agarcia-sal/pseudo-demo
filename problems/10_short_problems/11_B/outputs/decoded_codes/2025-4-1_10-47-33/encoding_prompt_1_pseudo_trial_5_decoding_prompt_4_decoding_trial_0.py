# Importing required libraries (if necessary) could be done here, but none are required for this code.

# Step 1: Input - Read an integer value from the user
targetNumber = abs(int(input()))  # Calculate the absolute value immediately after input

# Step 2: Initialize the counter variable
index = 0

# Step 3: Loop - Start an infinite loop
while True:
    # Calculate the sum of the first 'index' natural numbers
    currentSum = index * (index + 1) // 2  # Use integer division

    # Calculate the difference between currentSum and targetNumber
    difference = currentSum - targetNumber

    # Step 3.3: Check Conditions
    if currentSum == targetNumber:
        print(index)  # Output the index
        break  # Exit the loop
    elif currentSum > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index
            break  # Exit the loop
    
    # Increment the value of index by 1
    index += 1
