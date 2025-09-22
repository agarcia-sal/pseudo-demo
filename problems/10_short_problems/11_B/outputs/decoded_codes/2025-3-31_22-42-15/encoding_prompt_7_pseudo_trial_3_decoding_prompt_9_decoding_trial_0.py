def find_integer_based_on_sum(input_value):
    # Convert input to an absolute integer
    absolute_input = abs(input_value)
    
    # Initialize an index variable
    index = 0

    # Continuously loop to find a solution
    while True:
        # Calculate the sum of the first 'index' integers
        sum_value = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the absolute input
        difference = sum_value - absolute_input
        
        # Check if the sum is equal to the absolute input
        if sum_value == absolute_input:
            print(index)
            break  # Exit the loop since we have found our answer
            
        # Check if the sum is greater than the absolute input
        elif sum_value > absolute_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop since we have found our answer
        
        # Increment the index for the next iteration
        index += 1
