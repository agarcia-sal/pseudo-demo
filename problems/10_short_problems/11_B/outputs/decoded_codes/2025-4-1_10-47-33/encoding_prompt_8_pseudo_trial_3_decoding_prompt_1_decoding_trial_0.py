# 1. Initialize Variables
targetNumber = abs(int(input()))  # Getting the absolute value of the input
index = 0                          # Initialize index to 0

# 2. Start Infinite Loop
while True:

    # a. Calculate the Sum
    sumToIndex = (index * (index + 1)) / 2  # Using the formula for the sum of first n integers

    # b. Calculate the Difference
    difference = sumToIndex - targetNumber

    # c. Check for Exact Match
    if sumToIndex == targetNumber:
        print(index)  # Print the current number
        break  # Exit the loop

    # d. Check for Exceeding Value
    if sumToIndex > targetNumber:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the current number
            break  # Exit the loop

    # e. Increment Index
    index += 1  # Increase the value of index by 1
