# Get Input
targetNumber = abs(int(input()))  # Read a number from the user and store its absolute value

# Initialize Counter
counter = 0  # Counter to keep track of the current integer

# Start Infinite Loop
while True:
    # Calculate Sum
    currentSum = (counter * (counter + 1)) // 2  # Sum of the first 'counter' integers

    # Calculate Difference
    difference = currentSum - targetNumber  # Difference between currentSum and targetNumber

    # Check for Matching Sum
    if currentSum == targetNumber:
        print(counter)  # Print the counter if the sum matches the target
        break  # Exit the loop

    # Check for Exceeding Sum
    if currentSum > targetNumber:
        if difference % 2 == 0:  # Check if the difference is an even number
            print(counter)  # Print the counter if the difference is even
            break  # Exit the loop

    # Increment Counter
    counter += 1  # Increase the value of counter by 1
