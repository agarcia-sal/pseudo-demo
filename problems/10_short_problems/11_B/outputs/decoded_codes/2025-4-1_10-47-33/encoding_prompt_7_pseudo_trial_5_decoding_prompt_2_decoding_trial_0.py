def find_number_matching_condition():
    # Get the absolute value of input and convert it to an integer
    user_input = abs(int(input()))
    
    # Initialize the counter variable
    index = 0
    
    # Loop indefinitely until a break condition is met
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum = (index * (index + 1)) // 2
        
        # Calculate the difference between 'sum' and 'user_input'
        difference = sum - user_input
        
        # Check if the sum equals the user input
        if sum == user_input:
            print(index)
            break
        
        # Check if the sum exceeds the user input
        elif sum > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Call the function to execute
find_number_matching_condition()
