def find_integer_sum():
    # Initialize variables
    n = abs(int(input()))  # Get absolute value of user input
    i = 0  # This variable will represent the current integer
    s = 0  # Sum of the first i integers
    m = 0  # Difference between s and n

    # Infinite loop until break condition is met
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2
        # Determine the difference between s and n
        m = s - n

        # Check if s equals n
        if s == n:
            print(i)  # Output the current value of i
            break  # Exit the loop

        # Check if s exceeds n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Output the current value of i
                break  # Exit the loop

        # Move to the next integer
        i += 1

# Invoke the function
find_integer_sum()
