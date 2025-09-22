def find_triangular_number_index():
    # Get the absolute value of the integer input from the user
    user_input = abs(int(input()))
    
    # Initialize index variable
    index = 0
    
    # Repeat indefinitely
    while True:
        # Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the user input
        difference = triangular_number - user_input
        
        # Check if the triangular number equals the input
        if triangular_number == user_input:
            # Print the current index and exit the loop
            print(index)
            break
        
        # Check if the triangular number is greater than the user input
        elif triangular_number > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                # Print the current index and exit the loop
                print(index)
                break
        
        # Increment index for the next iteration
        index += 1

# Call the function to execute
find_triangular_number_index()
