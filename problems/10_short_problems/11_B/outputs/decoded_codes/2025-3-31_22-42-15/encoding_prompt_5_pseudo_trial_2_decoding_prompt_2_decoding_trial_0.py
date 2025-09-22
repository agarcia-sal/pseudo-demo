# Start Program

# Get User Input
targetNumber = abs(int(input()))

# Initialize Counter
currentIndex = 0

# Loop Until a Condition is Met
while True:
    # Calculate the sum of all integers from 0 to currentIndex
    currentSum = (currentIndex * (currentIndex + 1)) // 2
    
    # Calculate the difference
    difference = currentSum - targetNumber

    # Check Conditions
    if currentSum == targetNumber:
        # Print the answer
        print(currentIndex)
        break  # End the program
    
    if currentSum > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            # Print the answer
            print(currentIndex)
            break  # End the program
    
    # Increment currentIndex by 1
    currentIndex += 1

# End Program
