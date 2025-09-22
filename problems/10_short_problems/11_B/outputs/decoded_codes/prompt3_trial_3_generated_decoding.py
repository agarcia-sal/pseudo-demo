def find_index_for_absolute_value():
    # Read an integer input and take the absolute value
    absolute_value = abs(int(input()))

    # Initialize a counter variable
    index = 0 

    # Start an infinite loop
    while True:
        # Calculate the sum of the first 'index' natural numbers
        total_sum = (index * (index + 1)) // 2 
        
        # Calculate the difference between the sum and the input value
        difference = total_sum - absolute_value 
        
        # Check if the sum equals the input value
        if total_sum == absolute_value:
            print(index)
            break  # Exit the loop
        
        # Check if the sum is greater than the input value
        elif total_sum > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop
        
        # Increment the index to check the next natural number
        index += 1 

# Call the function to execute
find_index_for_absolute_value()
