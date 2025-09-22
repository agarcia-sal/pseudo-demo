def find_integer():
    # Initialize variable n as the absolute value of the integer input
    n = abs(int(input()))
    # Set variable i to 0
    i = 0

    while True:
        # Calculate the sum s as the sum of the first i integers
        s = i * (i + 1) // 2  # Using integer division

        # Calculate the difference m as s - n
        m = s - n

        # Check if sum s is equal to n
        if s == n:
            print(i)
            break  # Terminate the loop

        # Check if sum s is greater than n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)
                break  # Terminate the loop

        # Increment i by 1 for the next iteration
        i += 1

# Call the function to execute
find_integer()
