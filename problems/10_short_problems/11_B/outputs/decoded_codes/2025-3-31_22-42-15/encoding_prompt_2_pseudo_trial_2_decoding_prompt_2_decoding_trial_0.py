# Start
# Input: Read an integer value from the user and store its absolute value as targetSum
targetSum = abs(int(input()))

# Initialize: Set a counter index to 0
index = 0

# Loop: Begin an infinite loop
while True:
    # Calculate: Compute the sum of the first index natural numbers
    currentSum = index * (index + 1) // 2  # Using integer division for clarity

    # Calculate Difference
    difference = currentSum - targetSum

    # Check for Exact Match
    if currentSum == targetSum:
        # Output: Print the value of index
        print(index)
        # Terminate Loop
        break

    # Check for Overshoot
    if currentSum > targetSum:
        # Check Parity
        if difference % 2 == 0:  # If the difference is even
            # Output: Print the value of index
            print(index)
            # Terminate Loop
            break

    # Increment: Increase the value of index by 1
    index += 1

# End
