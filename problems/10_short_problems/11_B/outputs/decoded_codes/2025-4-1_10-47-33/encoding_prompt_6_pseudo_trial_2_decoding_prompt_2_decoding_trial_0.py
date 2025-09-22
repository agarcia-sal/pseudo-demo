# Start of the program

# Get the absolute value of a number input from the user
userInput = input()
n = abs(int(userInput))  # We convert input to an integer and take the absolute value
i = 0  # Initialize an index variable

while True:
    # Calculate the sum of the first i integers
    sumOfFirsti = (i * (i + 1)) // 2  # Use integer division for sum

    # Calculate the difference between the sum and n
    difference = sumOfFirsti - n

    # Check if the sum equals n
    if sumOfFirsti == n:
        print(i)  # Print the value of i
        break  # Exit the loop

    # Check if the sum is greater than n
    elif sumOfFirsti > n:
        # Check if the difference is even
        if difference % 2 == 0:
            print(i)  # Print the value of i
            break  # Exit the loop

    # Increment i for the next iteration
    i += 1

# End of the program
