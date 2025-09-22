# Start Program

# Get User Input
targetNumber = abs(int(input()))

# Initialize Counter
currentIndex = 0

# Loop Until a Condition is Met
while True:
    # Calculate the sum of all integers from 0 to currentIndex
    currentSum = sum(range(currentIndex + 1))
    
    # Calculate the difference between currentSum and targetNumber
    difference = currentSum - targetNumber

    # Check Conditions
    if currentSum == targetNumber:
        print(currentIndex)  # This is the answer
        break
    
    if currentSum > targetNumber:
        if difference % 2 == 0:  # Check if the difference is even
            print(currentIndex)  # This is also an answer
            break
    
    # Increment currentIndex by 1
    currentIndex += 1

# End Program
