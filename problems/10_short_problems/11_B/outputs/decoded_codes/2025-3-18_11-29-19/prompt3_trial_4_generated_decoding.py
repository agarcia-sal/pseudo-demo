def find_minimum_counter():
    # Read an integer input and take its absolute value
    user_input = abs(int(input()))
    
    # Initialize a variable to keep count
    counter = 0

    # Start an infinite loop to find the result
    while True:
        # Calculate the sum of the first 'counter' natural numbers
        sum_of_natural_numbers = (counter * (counter + 1)) // 2
        
        # Calculate the difference between the sum and user_input
        difference = sum_of_natural_numbers - user_input
        
        # Check if the calculated sum equals the user_input
        if sum_of_natural_numbers == user_input:
            # Print the current counter value and exit the loop
            print(counter)
            break
        
        # Check if the calculated sum exceeds user_input
        elif sum_of_natural_numbers > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                # Print the current counter value and exit the loop
                print(counter)
                break
        
        # Increment the counter for the next iteration
        counter += 1

# Call the function to execute the code
find_minimum_counter()
