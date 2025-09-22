def find_integer_sum():
    # Step 1: Initialize the main variables
    n = abs(int(input()))  # Get the absolute value of the input integer
    i = 0  # Start with the first integer

    # Step 2: Start an infinite loop for calculations
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2  # Use integer division
        
        # Calculate the difference between the current sum and n
        m = s - n

        # Check if the sum equals n
        if s == n:
            print(i)  # Output the current value of i
            break  # Exit the loop

        # Check if the sum is greater than n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the current value of i
                break  # Exit the loop

        # Increment i for the next iteration
        i += 1

# Call the function to execute
find_integer_sum()
