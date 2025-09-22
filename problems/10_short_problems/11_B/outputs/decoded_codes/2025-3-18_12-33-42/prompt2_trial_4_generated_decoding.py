# Start the program

# Receive input from the user and convert it to a non-negative integer called targetSum
targetSum = abs(int(input()))  # Taking absolute value to ensure non-negativity

# Initialize counter index to zero
index = 0

# Begin an infinite loop
while True:
    # Calculate the sum of the first `index` natural numbers
    currentSum = index * (index + 1) // 2  # Sum of the first `index` natural numbers
    # Determine the difference between currentSum and targetSum
    difference = currentSum - targetSum
    
    # Check if currentSum is equal to targetSum
    if currentSum == targetSum:
        # If true, output the value of index and exit the loop
        print(index)
        break
    
    # Check if currentSum is greater than targetSum
    if currentSum > targetSum:
        # If true, check if difference is even
        if difference % 2 == 0:
            # If true, output the value of index and exit the loop
            print(index)
            break
    
    # Increment index by one to examine the next natural number
    index += 1

# End the program (implicitly ends when the loop exits)
