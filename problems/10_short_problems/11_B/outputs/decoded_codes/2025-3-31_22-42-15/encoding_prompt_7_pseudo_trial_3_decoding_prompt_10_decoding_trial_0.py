def find_integer_based_on_sum(input_value):
    """
    This function finds and prints the smallest non-negative integer such that
    the sum of the first 'index' integers either equals the absolute input value
    or allows for an even difference between the sum and the absolute value.
    """
    # Convert input to an absolute integer
    absolute_input = abs(int(input_value))
    
    # Initialize an index variable
    index = 0

    # Continuously loop to find a solution
    while True:
        # Calculate the sum of the first 'index' integers
        sum_of_integers = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the absolute input
        difference = sum_of_integers - absolute_input
        
        # Check if the sum is equal to the absolute input
        if sum_of_integers == absolute_input:
            print(index)
            break  # Exit the loop since we have found our answer
            
        # Check if the sum is greater than the absolute input
        elif sum_of_integers > absolute_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop since we have found our answer
        
        # Increment the index for the next iteration
        index += 1

# Testing the function with different cases
if __name__ == "__main__":
    test_values = [10, -10, 3, 0, 15, 20]
    for value in test_values:
        find_integer_based_on_sum(value)
