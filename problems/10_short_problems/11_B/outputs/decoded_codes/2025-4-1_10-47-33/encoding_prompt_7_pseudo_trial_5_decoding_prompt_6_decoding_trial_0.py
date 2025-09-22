def find_number_matching_condition():
    # Get the absolute value of the user input and convert it to an integer
    user_input = abs(int(input()))
    
    # Initialize the counter variable
    index = 0
    
    # Loop indefinitely until a break condition is met
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_of_natural_numbers = (index * (index + 1)) // 2
        
        # Calculate the difference between 'sum_of_natural_numbers' and 'user_input'
        difference = sum_of_natural_numbers - user_input
        
        # Check if the sum equals the user input
        if sum_of_natural_numbers == user_input:
            print(index)
            break
        
        # Check if the sum exceeds the user input
        elif sum_of_natural_numbers > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Call the function to execute the code
find_number_matching_condition()
