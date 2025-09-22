# Start of the program

# Read an integer value from the user and take its absolute value
targetNumber = abs(int(input()))  # Ensure we take absolute value

# Initialize a variable currentIndex to 0
currentIndex = 0

# Enter an infinite loop
while True:
    # Calculate the sum of the first currentIndex natural numbers
    currentSum = currentIndex * (currentIndex + 1) // 2  # Use the formula for the sum of the first n natural numbers
    
    # Determine the difference between currentSum and targetNumber
    difference = currentSum - targetNumber
    
    # Check if currentSum is equal to targetNumber
    if currentSum == targetNumber:
        print(currentIndex)  # Display currentIndex as the result
        break  # Exit the loop
    
    # Check if currentSum is greater than targetNumber
    elif currentSum > targetNumber:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(currentIndex)  # Display currentIndex as the result
            break  # Exit the loop
    
    # Increment currentIndex by 1
    currentIndex += 1

# End of the program
