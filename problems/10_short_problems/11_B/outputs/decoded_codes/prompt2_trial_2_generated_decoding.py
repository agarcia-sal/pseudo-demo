# Step 1: Start the process by taking an input number representing a distance
targetDistance = abs(int(input()))

# Step 2: Initialize a variable called currentIndex to zero
currentIndex = 0

# Step 3: Enter an infinite loop
while True:
    # Step 3a: Calculate the triangular number corresponding to currentIndex
    triangularNumber = (currentIndex * (currentIndex + 1)) // 2  # Triangular number formula

    # Step 3b: Calculate the difference between triangularNumber and targetDistance
    difference = triangularNumber - targetDistance

    # Step 3c: Check if triangularNumber is equal to targetDistance
    if triangularNumber == targetDistance:
        print(currentIndex)  # Display the value of currentIndex as the result
        break  # Exit the loop

    # Step 3d: Check if triangularNumber is greater than targetDistance
    if triangularNumber > targetDistance:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(currentIndex)  # Display the value of currentIndex as the result
            break  # Exit the loop

    # Step 3e: If none of the above conditions are met, increment currentIndex
    currentIndex += 1
