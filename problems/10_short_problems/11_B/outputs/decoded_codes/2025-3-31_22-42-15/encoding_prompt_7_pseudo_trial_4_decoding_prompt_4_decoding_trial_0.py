def find_integer_with_specific_property():
    # Read input value from user
    input_value = int(input())
    absolute_value = abs(input_value)  # Get the absolute value of the input
    index = 0  # Initialize index to start from 0

    while True:
        # Calculate the sum of the first 'index' integers
        sum_of_first_index = (index * (index + 1)) // 2  # Using integer division
        
        # Calculate the difference from the absolute value
        difference = sum_of_first_index - absolute_value
        
        # Check if the sum equals the absolute value
        if sum_of_first_index == absolute_value:
            print(index)  # Print the index
            break  # Exit the loop
        
        # Check if the sum exceeds the absolute value
        elif sum_of_first_index > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the index
                break  # Exit the loop
        
        # Increment the index for the next iteration
        index += 1

# To execute the function
find_integer_with_specific_property()
