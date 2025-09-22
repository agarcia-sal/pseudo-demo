# Receive input
targetValue = abs(int(input()))  # Get the absolute value of the user's input

# Initialize a counter
counter = 0

# Begin an infinite loop
while True:
    # Calculate the sum of integers
    currentSum = counter * (counter + 1) // 2

    # Calculate the difference
    difference = currentSum - targetValue

    # Check equality
    if currentSum == targetValue:
        print(counter)  # Output counter as the solution
        break  # End the loop

    # Check exceedance condition
    if currentSum > targetValue:
        if difference % 2 == 0:  # Check if the difference is even
            print(counter)  # Output counter as the solution
            break  # End the loop

    # Increment counter
    counter += 1
