# Start
# Get input: Read an integer value from the user and store its absolute value in a variable called targetSum
targetSum = abs(int(input()))

# Initialize index: Set a variable index to 0
index = 0

# Repeat indefinitely
while True:
    # Calculate currentSum using the formula
    currentSum = (index * (index + 1)) / 2
    # Calculate the difference between currentSum and targetSum
    difference = currentSum - targetSum

    # Check if currentSum equals targetSum
    if currentSum == targetSum:
        print(index)
        break  # Exit the loop

    # Check if currentSum is greater than targetSum
    if currentSum > targetSum:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)
            break  # Exit the loop
    
    # Increment index
    index += 1
# End
