# Start of the program
n = abs(int(input()))  # Get the absolute value of an integer from user input and store in variable 'n'
i = 0  # Initialize variable 'i' to 0

# Infinite loop to find a solution
while True:
    # Calculate the sum of the first 'i' natural numbers
    s = i * (i + 1) // 2  # Use integer division for summation
    m = s - n  # Set 'm' to the difference between 's' and 'n'

    # Check if the current sum 's' equals 'n'
    if s == n:
        print(i)  # Output 'i' (the current value of i)
        break  # Exit the loop

    # Check if the current sum 's' exceeds 'n'
    elif s > n:
        # Check if the difference 'm' is even
        if m % 2 == 0:
            print(i)  # Output 'i' (the current value of i)
            break  # Exit the loop

    # Increment 'i' for the next iteration
    i += 1  # Increment 'i' by 1
# End of the program
