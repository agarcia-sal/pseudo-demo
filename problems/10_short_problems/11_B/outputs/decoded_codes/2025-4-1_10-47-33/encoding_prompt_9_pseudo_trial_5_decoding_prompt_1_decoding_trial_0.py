# Step 1: Receive and Prepare Input
targetNumber = int(input())  # Convert input to non-negative integer

# Step 2: Initialize Variables
currentIndex = 0

# Step 3: Process to Find the Desired Index
while True:  # Loop indefinitely
    # Calculate the triangular number
    triangularNumber = (currentIndex * (currentIndex + 1)) // 2
    # Calculate the difference
    difference = triangularNumber - targetNumber
    
    # Check if triangularNumber equals targetNumber
    if triangularNumber == targetNumber:
        print(currentIndex)  # Print the answer
        break  # Exit the loop
    # Otherwise, check if triangularNumber is greater than targetNumber
    elif triangularNumber > targetNumber:
        # Check if difference is even
        if difference % 2 == 0:
            print(currentIndex)  # Print the answer
            break  # Exit the loop
    
    # Increment currentIndex
    currentIndex += 1
