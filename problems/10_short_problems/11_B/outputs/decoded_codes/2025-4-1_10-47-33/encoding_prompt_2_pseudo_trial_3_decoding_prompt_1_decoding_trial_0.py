# 1. Start the program.
# (implied by the beginning of the script)

# 2. Receive an integer input from the user and take its absolute value. Store this value as targetNumber.
targetNumber = abs(int(input()))

# 3. Initialize a counter variable, currentIndex, to 0.
currentIndex = 0

# 4. Enter an infinite loop to perform the following steps:
while True:
    # a. Calculate the sum, sumValue, of all integers from 0 to currentIndex.
    sumValue = (currentIndex * (currentIndex + 1)) // 2

    # b. Determine the difference, differenceFromTarget, between sumValue and targetNumber.
    differenceFromTarget = sumValue - targetNumber

    # c. Check if sumValue is equal to targetNumber:
    if sumValue == targetNumber:
        print(currentIndex)  # print currentIndex and exit the loop
        break

    # d. If sumValue is greater than targetNumber, check if differenceFromTarget is even.
    if sumValue > targetNumber:
        if differenceFromTarget % 2 == 0:  # Check if the difference is even
            print(currentIndex)  # print currentIndex and exit the loop
            break

    # e. Increment currentIndex by 1.
    currentIndex += 1

# 5. End the program.
