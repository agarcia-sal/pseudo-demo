# Start the program.
targetNumber = abs(int(input()))  # Receive an integer input and take its absolute value
currentIndex = 0  # Initialize counter variable

while True:  # Enter an infinite loop
    sumValue = (currentIndex * (currentIndex + 1)) // 2  # Calculate sum from 0 to currentIndex
    differenceFromTarget = sumValue - targetNumber  # Determine the difference

    if sumValue == targetNumber:  # Check if sumValue is equal to targetNumber
        print(currentIndex)  # Print currentIndex and exit the loop
        break
    
    if sumValue > targetNumber:  # Check if sumValue is greater than targetNumber
        if differenceFromTarget % 2 == 0:  # Check if differenceFromTarget is even
            print(currentIndex)  # Print currentIndex and exit the loop
            break
    
    currentIndex += 1  # Increment currentIndex by 1
# End the program.
