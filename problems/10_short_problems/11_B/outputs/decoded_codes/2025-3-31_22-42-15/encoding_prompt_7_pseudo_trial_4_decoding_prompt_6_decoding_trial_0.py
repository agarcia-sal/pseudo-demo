def find_integer_with_specific_property():
    # Read input value and calculate its absolute value
    input_value = int(input())
    absolute_value = abs(input_value)
    index = 0

    while True:  # Start an infinite loop
        # Calculate the sum of the first 'index' integers
        sum_of_first_index = (index * (index + 1)) / 2
        difference = sum_of_first_index - absolute_value
        
        # Check if the sum equals the absolute value
        if sum_of_first_index == absolute_value:
            print(index)
            break
        
        # Check if the sum is greater than the absolute value
        elif sum_of_first_index > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next iteration
        index += 1

# Call the function
find_integer_with_specific_property()
