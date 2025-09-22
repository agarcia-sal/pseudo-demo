# Start of the program

# Get input and store its absolute value in targetSum
targetSum = abs(int(input()))

# Initialize index to 0
index = 0

# Repeat indefinitely until a condition to exit is met
while True:
    # Calculate the sum of the first `index` natural numbers
    currentSum = (index * (index + 1)) // 2  # using integer division

    # Calculate the difference between currentSum and targetSum
    difference = currentSum - targetSum

    # Check if currentSum equals targetSum
    if currentSum == targetSum:
        print(index)  # Print the current index
        break  # Exit the loop

    # Check if currentSum is greater than targetSum
    if currentSum > targetSum:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)  # Print the current index
            break  # Exit the loop
    
    # Increment index by 1 for the next iteration
    index += 1

# End of the program
