def find_smallest_integer():
    # Get the absolute value of the user input
    absolute_value = abs(int(input()))
    
    # Initialize the current index to zero
    current_index = 0
    
    while True:  # Start an indefinite loop
        # Calculate the sum of the first current_index natural numbers
        sum_of_numbers = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference from the absolute value
        difference = sum_of_numbers - absolute_value
        
        # Check if the sum matches the absolute value
        if sum_of_numbers == absolute_value:
            print(current_index)  # Print the current_index
            break  # Exit the loop
            
        # Check if the sum exceeds the absolute value
        elif sum_of_numbers > absolute_value:
            # If the difference is even, print current_index and exit
            if difference % 2 == 0:
                print(current_index)
                break  # Exit the loop
                
        # Increment current_index to check for the next natural number
        current_index += 1

# Call the function
find_smallest_integer()
