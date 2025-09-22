def find_minimum_integer(n):
    """
    This function finds the smallest non-negative integer `i` such that either
    the sum of the first `i` integers equals `n`, or the difference between
    that sum and `n` is an even number.

    Parameters:
    n (int): The target integer to match or use in the difference calculation.

    Returns:
    None: This function prints the result directly.
    """
    # Ensure n is a non-negative integer
    n = abs(int(n))
    
    # Initialize counter variable
    i = 0

    # Start an infinite loop
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2

        # Calculate the difference between sum s and n
        m = s - n

        # Check if sum s is equal to n
        if s == n:
            print(i)  # Output the current value of i
            break  # Exit the loop
        
        # Check if sum s exceeds n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Output the current value of i
                break  # Exit the loop
        
        # Increment counter for the next iteration
        i += 1

# Example usage (uncomment to test):
# user_input = input()     # Read an input from the user
# find_minimum_integer(user_input)
