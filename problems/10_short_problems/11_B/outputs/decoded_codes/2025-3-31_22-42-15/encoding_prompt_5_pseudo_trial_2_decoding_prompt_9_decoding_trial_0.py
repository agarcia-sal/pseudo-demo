# Start Program

# Get User Input
targetNumber = abs(int(input()))  # Read an integer input and take its absolute value

# Initialize Counter
currentIndex = 0

# Loop Until a Condition is Met
while True:
    # Calculate the sum of all integers from 0 to currentIndex
    currentSum = sum(range(currentIndex + 1))  # This gives the sum from 0 to currentIndex
    # Calculate the difference between currentSum and targetNumber
    difference = currentSum - targetNumber

    # Check Conditions
    if currentSum == targetNumber:
        print(currentIndex)  # Print currentIndex as the answer if sums match
        break  # End the program
    
    if currentSum > targetNumber:
        if difference % 2 == 0:  # Check if the difference is even
            print(currentIndex)  # Print currentIndex as the answer if difference is even
            break  # End the program
            
    # Increment currentIndex by 1
    currentIndex += 1

# End Program
