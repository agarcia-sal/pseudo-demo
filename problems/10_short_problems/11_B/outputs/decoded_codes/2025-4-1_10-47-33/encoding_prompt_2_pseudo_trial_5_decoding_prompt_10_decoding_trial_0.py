def find_smallest_integer():
    # Read integer input and store its absolute value
    absolute_value = abs(int(input()))
    
    index = 0  # Initialize the index for evaluating integers

    while True:  # Start an infinite loop to evaluate conditions
        # Calculate the sum of the first 'index' integers using the formula
        sum_of_integers = index * (index + 1) // 2
        # Calculate the difference between the sum_of_integers and absolute_value
        difference = sum_of_integers - absolute_value
        
        # Check if the sum_of_integers equals absolute_value
        if sum_of_integers == absolute_value:
            print(index)  # Print the resulting integer
            break  # Exit the loop
        
        # If sum_of_integers is greater than absolute_value
        if sum_of_integers > absolute_value:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)  # Print the resulting integer
                break  # Exit the loop
            
        # Increment index to evaluate the next integer
        index += 1

# Call the function to execute
find_smallest_integer()
