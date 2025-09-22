def find_index_for_absolute_value():
    # Read an integer input and store its absolute value
    number_to_find = abs(int(input()))
    
    # Initialize a counter variable
    index = 0
    
    # Infinite loop to find the required index
    while True:
        # Calculate the sum of the first 'index' natural numbers
        total_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the target number
        difference = total_sum - number_to_find
        
        # Check if the current sum equals the target number
        if total_sum == number_to_find:
            print(index)
            break
        
        # Check if the current sum exceeds the target number
        elif total_sum > number_to_find:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Call the function to execute
find_index_for_absolute_value()
