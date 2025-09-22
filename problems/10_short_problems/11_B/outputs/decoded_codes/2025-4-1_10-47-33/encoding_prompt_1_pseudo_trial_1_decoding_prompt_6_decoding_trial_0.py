# Start the program

# Get the absolute value of user input as an integer and assign it to 'n'
user_input = input()
n = abs(int(user_input))

# Initialize 'i' to 0
i = 0

# Enter an infinite loop
while True:
    # Calculate the sum 's' of the first 'i' natural numbers using the formula
    s = i * (i + 1) // 2  # Use integer division

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
    
    # Increment 'i' by 1
    i += 1

# End of program
