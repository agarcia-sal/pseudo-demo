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
        # Print currentIndex (this is the answer)
        print(currentIndex)
        # End the program
        break
        
    if currentSum > targetNumber:
        # Check if difference is even
        if difference % 2 == 0:
            # If it is even, print currentIndex (this is also an answer)
            print(currentIndex)
            # End the program
            break
    
    # Increment currentIndex by 1
    currentIndex += 1

# End Program
