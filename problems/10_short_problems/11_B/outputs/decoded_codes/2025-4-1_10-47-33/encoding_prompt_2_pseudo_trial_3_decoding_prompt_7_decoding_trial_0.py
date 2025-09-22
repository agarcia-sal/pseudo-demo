# Start the program

# Step 2: Receive an integer input from the user and take its absolute value
targetNumber = abs(int(input()))

# Step 3: Initialize a counter variable, currentIndex, to 0
currentIndex = 0

# Step 4: Enter an infinite loop to perform the necessary calculations
while True:
    # Step 4a: Calculate the sum of all integers from 0 to currentIndex
    sumValue = (currentIndex * (currentIndex + 1)) // 2  # Using integer division

    # Step 4b: Determine the difference from the target
    differenceFromTarget = sumValue - targetNumber

    # Step 4c: Check if sumValue is equal to targetNumber
    if sumValue == targetNumber:
        print(currentIndex)  # Print currentIndex if condition is met
        break  # Exit the loop

    # Step 4d: If sumValue is greater than targetNumber
    if sumValue > targetNumber:
        # Check if the difference is even
        if differenceFromTarget % 2 == 0:
            print(currentIndex)  # Print currentIndex if difference is even
            break  # Exit the loop

    # Step 4e: Increment currentIndex by 1
    currentIndex += 1

# Step 5: End the program (implicitly done when the program exits)
