def find_triangle_number_position():
    # Prompt user for an integer input
    user_input = int(input())
    
    # Set absolute value of the input
    absolute_value = abs(user_input)
    
    index = 0  # Initialize index to 0
    while True:  # Infinite loop to calculate triangular numbers
        # Calculate the nth triangular number
        triangle_number = (index * (index + 1)) // 2
        # Calculate the difference between the triangular number and absolute value
        difference = triangle_number - absolute_value
        
        # Check if the triangular number matches the absolute value
        if triangle_number == absolute_value:
            print(index)  # Output the index if it matches
            break  # Exit the loop
        
        # Check if the triangular number is greater than the absolute value
        elif triangle_number > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index if the difference is even
                break  # Exit the loop
        
        index += 1  # Increment index to check the next triangular number

# Call the function to execute
find_triangle_number_position()
