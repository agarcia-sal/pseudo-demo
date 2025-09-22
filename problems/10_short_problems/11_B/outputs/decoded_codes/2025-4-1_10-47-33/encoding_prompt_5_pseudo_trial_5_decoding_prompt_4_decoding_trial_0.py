def find_triangular_number_index():
    # Read user input as an absolute value
    target_number = abs(int(input()))
    
    index = 0  # Initialize the index for triangular numbers
    
    while True:  # Loop indefinitely until we find the solution
        # Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2  # Use integer division
        
        # Calculate the difference between the triangular number and the target
        difference = triangular_number - target_number
        
        # Check if the triangular number matches the target number
        if triangular_number == target_number:
            print(index)  # Output the index if there's an exact match
            break  # Exit the loop
        # Check if the triangular number exceeds the target number
        elif triangular_number > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index if the difference is even
                break  # Exit the loop
        
        index += 1  # Increment the index to check the next triangular number

# Run the function to start the program
find_triangular_number_index()
