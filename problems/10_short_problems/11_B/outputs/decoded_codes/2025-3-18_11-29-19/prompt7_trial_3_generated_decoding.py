def find_integer():
    # Convert input to a positive integer
    n = abs(int(input()))
    # Initialize counter i to 0
    i = 0

    # Infinite loop to find the integer
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2  # Using integer division for sum
        m = s - n  # Calculate the difference

        # Check if the current sum is equal to n
        if s == n:
            print(i)  # Output the current value of i
            break  # Exit the loop
        
        # Check if the current sum exceeds n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the current value of i
                break  # Exit the loop
        
        # Increment the counter to check the next integer
        i += 1

# This function can be tested with various inputs to ensure robustness.
