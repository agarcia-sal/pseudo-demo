def find_integer():
    # Read an integer input and convert to absolute value
    n = abs(int(input()))

    # Initialize a counter variable
    i = 0

    # Infinite loop to increment counter until a condition is met
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Using integer division

        # Calculate the difference from n
        m = s - n

        # Check if the sum equals n
        if s == n:
            # Print the current value of i as result
            print(i)
            break
        
        # Check if the sum exceeds n
        elif s > n:
            # If the difference is even
            if m % 2 == 0:
                # Print the current value of i as result
                print(i)
                break
        
        # Increment the counter for the next iteration
        i += 1

# Call the function to execute it
find_integer()
