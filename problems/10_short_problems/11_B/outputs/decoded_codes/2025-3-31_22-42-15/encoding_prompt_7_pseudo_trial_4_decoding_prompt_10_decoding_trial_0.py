def find_integer_with_specific_property(input_value):
    # Initialize the absolute value of the input
    absolute_value = abs(input_value)
    index = 0  # Start with an index of 0
    
    while True:
        # Calculate the sum of the first 'index' integers using the formula
        sum_of_first_index = (index * (index + 1)) // 2
        difference = sum_of_first_index - absolute_value  # Calculate the difference

        # Check if the sum equals the absolute value
        if sum_of_first_index == absolute_value:
            print(index)
            break
        
        # Check if the sum has surpassed the absolute value
        elif sum_of_first_index > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        index += 1  # Increment the index for the next iteration

# Example usage
input_value = int(input())
find_integer_with_specific_property(input_value)
