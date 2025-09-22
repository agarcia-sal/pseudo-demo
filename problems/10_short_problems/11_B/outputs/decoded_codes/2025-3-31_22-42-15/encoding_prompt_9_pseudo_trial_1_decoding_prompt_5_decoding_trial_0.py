# Function to find the least non-negative integer whose triangular number is equal to or exceeds the given integer
def find_least_integer():
    # Read the input and convert it to an integer
    absolute_value = abs(int(input()))
    index = 0  # Initialize index for calculating triangular numbers

    # Repeat indefinitely until we find the desired index
    while True:
        # Calculate the triangular number using the formula: T(n) = n(n + 1)/2
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the absolute value
        difference = triangular_number - absolute_value
        
        # Check if the triangular number is equal to the absolute value
        if triangular_number == absolute_value:
            print(index)  # Output the index
            break  # Exit the loop
            
        # Check if the triangular number exceeds the absolute value
        if triangular_number > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break  # Exit the loop
        
        # Increment the index for the next iteration
        index += 1

# The function can be called as follows:
# find_least_integer()

# Note for testing: Test with different inputs for edge cases such as 0, 1, 2, 3, and larger numbers.
