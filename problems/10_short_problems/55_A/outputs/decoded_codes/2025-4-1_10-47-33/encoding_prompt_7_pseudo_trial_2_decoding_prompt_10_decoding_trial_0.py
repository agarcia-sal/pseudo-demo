def check_status_of_elements(n):
    # Initialize an array 'b' of size n with all values set to True
    b = [True] * n
    index_j = 0
    counter_i = 1

    # Process elements while counter_i is less than or equal to 500000
    while counter_i <= 500000:
        if b[index_j]:  # If element at index_j in array b is True
            b[index_j] = False  # Mark it as False

        counter_i += 1  # Increment counter_i by 1
        index_j = (index_j + counter_i) % n  # Update index_j

    # Create a new array 'x' containing all True values from array 'b'
    x = [value for value in b if value]

    # Output result based on the length of x
    if len(x) == 0:
        print("YES")  # All elements in 'b' have been set to False
    else:
        print("NO")   # There are still True elements in 'b'

# Example usage:
# To run the function, simply call it with a specific value of n
n = int(input())
check_status_of_elements(n)


# Testing edge cases
check_status_of_elements(0)  # Expectation might be refined
check_status_of_elements(1)  # Test with minimum size
check_status_of_elements(100) # General case
