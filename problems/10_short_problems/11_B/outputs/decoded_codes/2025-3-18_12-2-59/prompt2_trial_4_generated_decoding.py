# Start
# Define a variable to hold the absolute value of an integer input by the user
targetValue = abs(int(input()))

# Initialize Counter
index = 0  # This counter will be used to track the current position in our calculations

# Continuous Loop
while True:
    # Calculate Sum
    triangularSum = (index * (index + 1)) // 2  # Triangular number formula: n(n + 1)/2
    
    # Determine Difference
    difference = triangularSum - targetValue

    # Check Conditions
    if triangularSum == targetValue:
        # Output the current value of index as it represents a valid solution
        print(index)
        break  # Exit the loop
    elif triangularSum > targetValue:
        # Check if difference is even
        if difference % 2 == 0:
            # Output the current value of index as it represents another valid solution
            print(index)
            break  # Exit the loop

    # Update Counter
    index += 1  # Increment the index by 1 to continue the loop with the next integer

# End
