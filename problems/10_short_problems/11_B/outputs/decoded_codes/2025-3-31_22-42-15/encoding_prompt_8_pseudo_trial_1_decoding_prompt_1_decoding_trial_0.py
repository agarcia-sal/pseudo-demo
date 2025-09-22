# Step 1: Obtain a positive integer from the user
targetValue = abs(int(input()))  # Store the absolute value in 'targetValue'

# Step 2: Initialize 'currentIndex' to 0
currentIndex = 0

# Step 3: Begin an infinite loop to calculate triangular numbers
while True:
    # Step 3a: Calculate the triangular number for 'currentIndex'
    triangularNumber = (currentIndex * (currentIndex + 1)) // 2  # Using // for integer division

    # Step 3b: Calculate the difference between the triangular number and 'targetValue'
    difference = triangularNumber - targetValue

    # Step 3c: Check if the triangular number equals the targetValue
    if triangularNumber == targetValue:
        print(currentIndex)  # Print the currentIndex
        break  # Exit the loop

    # Step 3d: Check if the triangular number is greater than the targetValue
    if triangularNumber > targetValue:
        # Check if the difference is an even number
        if difference % 2 == 0:  # Check if remainder when divided by 2 is 0
            print(currentIndex)  # Print the currentIndex
            break  # Exit the loop

    # Step 3e: Increment 'currentIndex' by 1 to check the next triangular number
    currentIndex += 1
