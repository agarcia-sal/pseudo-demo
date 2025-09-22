# Receive and prepare input
targetNumber = int(input())  # Read the user input and convert it to a non-negative integer

# Initialize variables
currentIndex = 0

# Process to find the desired index
while True:
    # Calculate the triangular number
    triangularNumber = (currentIndex * (currentIndex + 1)) // 2
    # Calculate the difference
    difference = triangularNumber - targetNumber

    # Check if triangularNumber equals targetNumber
    if triangularNumber == targetNumber:
        print(currentIndex)  # Print the answer
        break
    
    # Check if triangularNumber is greater than targetNumber
    if triangularNumber > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(currentIndex)  # Print the answer
            break
    
    # Increment currentIndex by 1
    currentIndex += 1
