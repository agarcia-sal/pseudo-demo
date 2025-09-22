def find_triangular_number_index():
    # Read input from the user and convert it to a non-negative integer
    target_number = abs(int(input()))
    
    # Initialize the counter for the triangular number index
    index = 0
    
    # Loop indefinitely to compute triangular numbers
    while True:
        # Calculate the triangular number using the formula
        triangular_number = (index * (index + 1)) // 2
        difference = triangular_number - target_number
        
        # Check if the triangular number matches the target number
        if triangular_number == target_number:
            print(index)  # Output the index
            break
        # Check if the triangular number is greater than the target number
        elif triangular_number > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break
        
        # Increment the index for the next iteration
        index += 1

# Call the function to execute the program
find_triangular_number_index()
