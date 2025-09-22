def find_largest_i():
    # Input: Read an integer value and get its absolute value
    n = abs(int(input()))  # Reading user input and converting to absolute value

    # Initialize a counter variable
    i = 0

    # Loop indefinitely until a break condition is met
    while True:
        # Calculate the sum of the first 'i' natural numbers
        s = i * (i + 1) // 2  # Use integer division for accuracy
        
        # Calculate the difference between the current sum and 'n'
        m = s - n
        
        # Check if the sum is exactly equal to 'n'
        if s == n:
            print(i)  # Output the value of 'i'
            break
        
        # Check if the current sum exceeds 'n'
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the value of 'i'
                break

        # Increment the counter variable
        i += 1  # Increment i by 1

# Call the function to execute
find_largest_i()
