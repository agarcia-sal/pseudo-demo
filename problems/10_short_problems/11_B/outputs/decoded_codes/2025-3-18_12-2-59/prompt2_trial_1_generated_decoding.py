# Start the Process

# Take an Input
targetNumber = abs(int(input()))  # Obtain a number and convert it to its absolute integer value

# Initialize a Counter
index = 0  # Set a variable 'index' to 0

# Begin an Infinite Loop
while True:
    # Calculate the Sum of Natural Numbers
    sumOfIndex = (index * (index + 1)) / 2  # Compute the sum of the first 'index' numbers

    # Calculate the Difference
    difference = sumOfIndex - targetNumber  # Determine the difference

    # Check for Exact Match
    if sumOfIndex == targetNumber:
        print(index)  # Output the current 'index' value
        break  # Exit the loop

    # Check if Sum Exceeds Target
    if sumOfIndex > targetNumber:
        # Further check the 'difference'
        if difference % 2 == 0:  # If 'difference' is even
            print(index)  # Output the current 'index' value
            break  # Exit the loop

    # Increment the Counter
    index += 1  # Increase 'index' by 1
