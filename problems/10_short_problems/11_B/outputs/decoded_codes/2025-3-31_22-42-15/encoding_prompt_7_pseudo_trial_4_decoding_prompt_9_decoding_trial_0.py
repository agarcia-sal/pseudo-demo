def find_integer_with_specific_property():
    input_value = int(input())  # Reading the input value
    absolute_value = abs(input_value)  # Taking the absolute value
    index = 0  # Initialize index to 0
    
    while True:
        sum_of_first_index = (index * (index + 1)) / 2  # Calculate the sum of the first index integers
        difference = sum_of_first_index - absolute_value  # Calculate the difference
        
        # Check if the sum equals the absolute value
        if sum_of_first_index == absolute_value:
            print(index)  # Print the index
            break  # Exit the loop
        
        # Check if the sum is greater than the absolute value
        elif sum_of_first_index > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the index
                break  # Exit the loop
        
        index += 1  # Increment the index by 1
