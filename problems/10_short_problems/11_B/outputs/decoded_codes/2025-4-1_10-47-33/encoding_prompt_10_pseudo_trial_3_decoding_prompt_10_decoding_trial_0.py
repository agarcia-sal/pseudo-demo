def find_integer_for_sum_of_n():
    # Get the absolute value of the user input
    n = abs(int(input()))
    i = 0  # Initialize the counter

    # Start an infinite loop
    while True:
        # Calculate the sum of the first 'i' integers
        s = (i * (i + 1)) // 2  # Use integer division for accuracy
        m = s - n  # Difference between the sum 's' and 'n'

        # Check if the calculated sum 's' equals 'n'
        if s == n:
            print(i)  # Output the value of 'i' if sums are equal
            break  # Exit the loop

        # Check if 's' is greater than 'n'
        elif s > n:
            # Check if the difference 'm' is even
            if m % 2 == 0:
                print(i)  # Output the value of 'i' if 'm' is even
                break  # Exit the loop

        # Increment 'i' for the next iteration
        i += 1

# Call the function to execute the code
find_integer_for_sum_of_n()
