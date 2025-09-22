# Get input from the user
targetNumber = abs(int(input()))  # Take the absolute value of the input number

# Initialize variables
index = 0  # This variable will represent the current integer we are checking

# Loop to find valid index
while True:  # Continue indefinitely until a valid index is found
    # Calculate the sum of the first 'index' integers
    currentSum = (index * (index + 1)) // 2  # Use integer division for clarity

    # Compute the difference between currentSum and targetNumber
    difference = currentSum - targetNumber

    # Check conditions
    if currentSum == targetNumber:  # If the sum equals the target number
        print(index)  # Output the index
        break  # Exit the loop
    elif currentSum > targetNumber:  # If the sum exceeds the target number
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Output the index
            break  # Exit the loop

    # Increment index to check the next integer
    index += 1
