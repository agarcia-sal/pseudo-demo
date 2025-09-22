# Purpose: Find the smallest non-negative integer whose triangular number equals or exceeds a given input number.

# Step 1: Receive and prepare input
targetNumber = int(input())  # Read user input and convert to integer

# Step 2: Initialize variables
currentIndex = 0  # Holds the current index to calculate triangular numbers

# Step 3: Process to find the desired index
while True:  # Infinite loop to calculate triangular numbers
    # Calculate the triangular number using the formula
    triangularNumber = (currentIndex * (currentIndex + 1)) // 2  # Triangular number formula

    # Calculate the difference
    difference = triangularNumber - targetNumber  # Difference between triangular number and target

    # Check if the triangular number equals the target number
    if triangularNumber == targetNumber:
        print(currentIndex)  # Print the result and exit
        break  # Exit the loop
    
    # Check if triangular number is greater than the target number
    elif triangularNumber > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(currentIndex)  # Print the result and exit
            break  # Exit the loop

    # Increment index for the next triangular number calculation
    currentIndex += 1  # Move to the next index
