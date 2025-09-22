# Get input from the user and store its absolute value in 'targetNumber'
targetNumber = abs(int(input()))

# Initialize a counter to track the current integer
counter = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first 'counter' integers
    currentSum = (counter * (counter + 1)) // 2

    # Calculate the difference between currentSum and targetNumber
    difference = currentSum - targetNumber

    # Check if the currentSum equals targetNumber
    if currentSum == targetNumber:
        print(counter)
        break

    # Check if currentSum exceeds targetNumber
    if currentSum > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(counter)
            break

    # Increment the counter by 1
    counter += 1
