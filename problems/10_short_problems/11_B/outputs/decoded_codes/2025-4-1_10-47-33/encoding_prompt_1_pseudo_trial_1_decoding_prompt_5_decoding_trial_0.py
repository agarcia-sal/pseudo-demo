# Start the program
# Get the absolute value of user input as an integer
n = abs(int(input()))

# Initialize the counter for natural numbers
i = 0

# Enter an infinite loop
while True:
    # Calculate the sum 's' of the first 'i' natural numbers
    s = i * (i + 1) // 2  # using integer division for accuracy

    # Calculate the difference 'm' between 's' and 'n'
    m = s - n

    # Check if 's' is equal to 'n'
    if s == n:
        print(i)  # Print the value of 'i' and exit the loop
        break

    # Check if 's' is greater than 'n'
    if s > n:
        # Check if 'm' is even
        if m % 2 == 0:
            print(i)  # Print the value of 'i' and exit the loop
            break

    # Increment the counter
    i += 1

# End of program
