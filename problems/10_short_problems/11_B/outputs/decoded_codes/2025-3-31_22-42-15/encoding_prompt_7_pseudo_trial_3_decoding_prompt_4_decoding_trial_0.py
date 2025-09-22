def find_integer_based_on_sum(input_value):
    # Convert input to an absolute integer
    absolute_input = abs(int(input_value))
    
    # Initialize an index variable
    index = 0

    # Continuously loop to find a solution
    while True:
        # Calculate the sum of the first 'index' integers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the absolute input
        difference = current_sum - absolute_input
        
        # Check if the sum is equal to the absolute input
        if current_sum == absolute_input:
            print(index)
            break  # Exit the loop since we have found our answer
            
        # Check if the sum is greater than the absolute input
        elif current_sum > absolute_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop since we have found our answer
        
        # Increment the index for the next iteration
        index += 1

# Example usage:
input_value = input()  # User provides input without prompt
find_integer_based_on_sum(input_value)
