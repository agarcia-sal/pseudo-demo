# Start of the program

# Input: Read an integer value from the user and store its absolute value as targetSum
targetSum = abs(int(input()))

# Initialize: Set a counter index to 0
index = 0

# Loop: An infinite loop that continues until a break condition is met
while True:
    # Calculate: Compute the sum of the first index natural numbers
    currentSum = index * (index + 1) // 2
    
    # Calculate Difference
    difference = currentSum - targetSum

    # Check for Exact Match
    if currentSum == targetSum:
        # Output: Print the value of index
        print(index)
        break  # Terminate Loop

    # Check for Overshoot
    if currentSum > targetSum:
        # Check Parity
        if difference % 2 == 0:
            # Output: Print the value of index
            print(index)
            break  # Terminate Loop

    # Increment: Increase the value of index by 1
    index += 1

# End of the program
