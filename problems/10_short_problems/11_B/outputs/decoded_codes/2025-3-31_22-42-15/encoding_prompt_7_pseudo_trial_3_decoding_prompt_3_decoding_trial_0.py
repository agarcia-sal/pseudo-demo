def find_integer_based_on_sum():
    # Read input and convert to absolute integer
    input_value = abs(int(input()))
    
    # Initialize an index variable
    index = 0

    # Continuously loop to find a solution
    while True:
        # Calculate the sum of the first 'index' integers
        sum_of_integers = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the absolute input
        difference = sum_of_integers - input_value
        
        # Check if the sum matches the absolute input
        if sum_of_integers == input_value:
            print(index)
            break  # Exit the loop since we have found our answer
        
        # Check if the sum is greater than the absolute input
        elif sum_of_integers > input_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop since we have found our answer
        
        # Increment the index for the next iteration
        index += 1

# Call the function to execute
find_integer_based_on_sum()
