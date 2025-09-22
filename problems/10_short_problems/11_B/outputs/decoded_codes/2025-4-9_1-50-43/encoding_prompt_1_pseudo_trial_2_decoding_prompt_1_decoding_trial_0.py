# 1. Start the program (implicitly handled by Python's execution)

# 2. Get user input and convert it to a non-negative integer
inputNumber = abs(int(input()))

# 3. Initialize variable index to 0
index = 0  # This variable will represent the current triangular number index

# 4. Continuously perform the following steps until a condition is met:
while True:
    # a. Calculate the current triangular number
    triangularNumber = (index * (index + 1)) / 2  # Formula for triangular number

    # b. Calculate the difference between the current triangular number and inputNumber
    difference = triangularNumber - inputNumber

    # c. Check if the triangular number is equal to the inputNumber
    if triangularNumber == inputNumber:
        print(index)  # Output the index if the condition is satisfied
        break  # Stop processing

    # d. Check if the triangular number is greater than the inputNumber
    if triangularNumber > inputNumber:
        # CHECK if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the index if this condition is satisfied
            break  # Stop processing

    # e. Increment the index by 1 to check the next triangular number
    index += 1

# 5. End the program (implicitly handled by Python's execution)
