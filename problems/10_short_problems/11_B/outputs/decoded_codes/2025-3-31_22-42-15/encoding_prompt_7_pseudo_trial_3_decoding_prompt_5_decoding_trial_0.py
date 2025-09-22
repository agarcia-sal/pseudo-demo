def find_integer_based_on_sum():
    # Get user input and convert it to an absolute integer
    input_value = int(input())
    absolute_input = abs(input_value)
    
    # Initialize an index variable
    index = 0

    # Continuously loop to find a solution
    while True:
        
        # Calculate the sum of the first 'index' integers using the formula
        calculated_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the absolute input
        difference = calculated_sum - absolute_input
        
        # Check if the sum is equal to the absolute input
        if calculated_sum == absolute_input:
            print(index)
            break  # Exit the loop since we have found our answer
            
        # Check if the sum is greater than the absolute input
        elif calculated_sum > absolute_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop since we have found our answer
        
        # Increment the index for the next iteration
        index += 1

# Example test case
# You can test the function by providing various input values.
# Uncomment the line below to run the function.
# find_integer_based_on_sum()
