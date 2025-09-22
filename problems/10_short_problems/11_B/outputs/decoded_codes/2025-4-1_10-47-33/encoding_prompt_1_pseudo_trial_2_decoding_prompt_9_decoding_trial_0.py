# Read a number from the user and store its absolute value in a variable
absoluteInput = abs(int(input()))

# Initialize a counter to keep track of the current integer
index = 0

# Infinite loop for calculation
while True:
    # Calculate the sum of the first 'index' integers
    currentSum = (index * (index + 1)) / 2
    # Calculate the difference between currentSum and absoluteInput
    difference = currentSum - absoluteInput
    
    # Check conditions
    if currentSum == absoluteInput:
        # Output the value of index as the result
        print(index)
        break
    if currentSum > absoluteInput:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # Output the value of index as the result
            print(index)
            break

    # Increment the counter to consider the next integer
    index += 1
