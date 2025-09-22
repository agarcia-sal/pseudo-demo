# Purpose: To find the smallest non-negative integer whose sum of consecutive integers starting from zero
# either equals a given number or exceeds it by an even number.

# Start Program

# Get User Input
targetNumber = int(input())  # Read an integer input from the user
targetNumber = abs(targetNumber)  # Convert the input to its absolute value

# Initialize Counter
currentIndex = 0  # Start with the index at 0

# Loop Until a Condition is Met
while True:
    # Calculate the sum of all integers from 0 to currentIndex
    currentSum = (currentIndex * (currentIndex + 1)) // 2  # Using the formula for the sum of the first n integers
    
    # Calculate the difference between currentSum and targetNumber
    difference = currentSum - targetNumber
    
    # Check Conditions
    if currentSum == targetNumber:
        # If currentSum is equal to targetNumber, print currentIndex and end the program
        print(currentIndex)
        break
    
    if currentSum > targetNumber:
        # If currentSum is greater than targetNumber, check if the difference is even
        if difference % 2 == 0:
            # If the difference is even, print currentIndex and end the program
            print(currentIndex)
            break
    
    # Increment currentIndex by 1
    currentIndex += 1

# End Program
