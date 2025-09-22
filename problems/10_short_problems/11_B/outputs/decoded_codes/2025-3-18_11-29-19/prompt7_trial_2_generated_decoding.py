def find_number_for_triangle_number():
    # Get the absolute value of the user's input and convert it to an integer
    user_input = abs(int(input()))
    
    index = 0  # This will track the current triangular number's position

    while True:
        # Calculate the current triangular number using the formula n(n + 1) / 2
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the current triangular number and the input
        difference = triangular_number - user_input
        
        # Check if the current triangular number equals the user input
        if triangular_number == user_input:
            print(index)  # Output the current index
            break  # Exit the loop

        # Check if the current triangular number exceeds the user input
        elif triangular_number > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop
        
        # Increment the index for the next triangular number calculation
        index += 1

# Calling the function to execute it
find_number_for_triangle_number()
