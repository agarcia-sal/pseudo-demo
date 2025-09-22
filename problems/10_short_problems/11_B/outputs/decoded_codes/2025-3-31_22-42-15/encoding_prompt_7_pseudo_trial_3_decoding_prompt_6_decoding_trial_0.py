def find_integer_based_on_sum():
    # Read the input value and convert it to an absolute integer
    input_value = int(input())
    absolute_input = abs(input_value)

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

# Call the function to execute the logic
find_integer_based_on_sum()
