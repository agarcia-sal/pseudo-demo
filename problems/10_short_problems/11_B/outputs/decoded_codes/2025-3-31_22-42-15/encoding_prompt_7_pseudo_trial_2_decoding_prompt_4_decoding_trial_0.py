def find_minimum_integer(n):
    # Ensure n is a non-negative integer
    n = abs(int(n))

    # Initialize counter variable
    i = 0

    # Start an infinite loop
    while True:
        # Calculate the sum of the first i integers
        sum_i = (i * (i + 1)) // 2
        
        # Calculate the difference between sum_i and n
        difference = sum_i - n
        
        # Check if sum_i is equal to n
        if sum_i == n:
            print(i)  # Output the current value of i
            break  # Exit the loop
        
        # Check if sum_i exceeds n
        elif sum_i > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)  # Output the current value of i
                break  # Exit the loop
        
        # Increment counter for the next iteration
        i += 1

# Example usage:
# Uncomment the following lines to test the function
# find_minimum_integer(input())
