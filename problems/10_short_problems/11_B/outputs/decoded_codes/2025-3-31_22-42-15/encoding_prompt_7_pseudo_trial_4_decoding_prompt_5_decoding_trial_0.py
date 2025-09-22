def find_integer_with_specific_property():
    # Read input value from the user
    input_value = int(input())
    
    # Calculate the absolute value of the input
    absolute_value = abs(input_value)
    index = 0  # Initialize index
    
    while True:
        # Calculate the sum of the first 'index' integers
        sum_of_first_index = (index * (index + 1)) // 2
        difference = sum_of_first_index - absolute_value
        
        # Check if the sum equals the absolute value
        if sum_of_first_index == absolute_value:
            print(index)
            break
        
        # Check if the sum is greater than the absolute value
        elif sum_of_first_index > absolute_value:
            # If the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next iteration
        index += 1

# Example test cases (uncomment to test)
# find_integer_with_specific_property()  # For example input: 3 (output should be 2)
# find_integer_with_specific_property()  # For example input: -5 (output should be 5)
