def find_integer_with_specific_property():
    # Read input value from user
    input_value = int(input())
    
    # Calculate absolute value
    absolute_value = abs(input_value)
    index = 0
    
    while True:
        # Calculate the sum of the first 'index' integers
        sum_of_first_index = (index * (index + 1)) // 2
        
        # Calculate the difference
        difference = sum_of_first_index - absolute_value
        
        # Check if the sum equals the absolute value
        if sum_of_first_index == absolute_value:
            print(index)
            break
        
        # Check if the sum exceeds the absolute value
        elif sum_of_first_index > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index by 1 for the next loop iteration
        index += 1
