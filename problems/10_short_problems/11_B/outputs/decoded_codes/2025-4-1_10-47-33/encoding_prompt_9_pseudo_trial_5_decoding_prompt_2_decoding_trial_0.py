# Step 1: Receive and Prepare Input
targetNumber = int(input())

# Step 2: Initialize Variables
currentIndex = 0

# Step 3: Process to Find the Desired Index
while True:
    # Calculate the triangular number
    triangularNumber = (currentIndex * (currentIndex + 1)) // 2
    
    # Calculate the difference
    difference = triangularNumber - targetNumber
    
    # Check if triangularNumber equals targetNumber
    if triangularNumber == targetNumber:
        print(currentIndex)  # This is the answer
        break
    
    # Check if triangularNumber is greater than targetNumber
    if triangularNumber > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(currentIndex)  # This is the answer
            break

    # Increment currentIndex by 1
    currentIndex += 1
