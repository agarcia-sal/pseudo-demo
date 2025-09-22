def findMinimumInteger(n):
    # Ensure n is a non-negative integer
    n = abs(int(input()))  # Read input and convert to absolute integer

    # Initialize counter variable
    i = 0

    # Start an infinite loop
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2  # Use integer division for sum

        # Calculate the difference between sum s and n
        m = s - n

        # Check if sum s is equal to n
        if s == n:
            print(i)  # Output the current value of i
            break  # Exit the loop

        # Check if sum s exceeds n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:  # Check if m is even
                print(i)  # Output the current value of i
                break  # Exit the loop

        # Increment counter for the next iteration
        i += 1

# To execute the function, uncomment the line below
# findMinimumInteger()
