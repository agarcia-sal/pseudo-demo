def find_minimal_integer():
    # Prompt the user for an integer input and take its absolute value
    user_input = abs(int(input()))
    
    # Initialize a counter to keep track of the current integer
    current_integer = 0

    # Enter an infinite loop to find the required integer
    while True:
        # Calculate the sum of the first current_integer numbers
        sum_integers = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference between the sum and user_input
        difference = sum_integers - user_input
        
        # Check if the calculated sum equals user_input
        if sum_integers == user_input:
            # Print the current integer and exit the loop
            print(current_integer)
            break
        
        # Check if the calculated sum exceeds user_input
        elif sum_integers > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                # Print the current integer and exit the loop
                print(current_integer)
                break
        
        # Increment the counter for the next iteration
        current_integer += 1

# Call the function to execute
find_minimal_integer()
