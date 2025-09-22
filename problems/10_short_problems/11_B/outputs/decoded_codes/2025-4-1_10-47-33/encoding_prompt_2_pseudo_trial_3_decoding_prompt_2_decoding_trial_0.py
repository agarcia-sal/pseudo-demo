# Step 1: Start the program (implicitly done)

# Step 2: Receive an integer input from the user and take its absolute value
targetNumber = abs(int(input()))

# Step 3: Initialize a counter variable, currentIndex, to 0
currentIndex = 0

# Step 4: Enter an infinite loop
while True:
    # Step 4a: Calculate the sum, sumValue, of all integers from 0 to currentIndex
    sumValue = (currentIndex * (currentIndex + 1)) // 2
    
    # Step 4b: Determine the difference, differenceFromTarget
    differenceFromTarget = sumValue - targetNumber
    
    # Step 4c: Check if sumValue is equal to targetNumber
    if sumValue == targetNumber:
        print(currentIndex)
        break  # exit the loop
    
    # Step 4d: Check if sumValue is greater than targetNumber
    if sumValue > targetNumber:
        # Step 4d: Check if differenceFromTarget is even
        if differenceFromTarget % 2 == 0:
            print(currentIndex)
            break  # exit the loop
    
    # Step 4e: Increment currentIndex by 1
    currentIndex += 1

# Step 5: End the program (implicitly done)
