def find_triangular_index():
    # Obtain a positive integer from the user
    target_value = abs(int(input()))  # Convert input to an absolute integer

    current_index = 0  # Initialize the index for triangular number calculation

    while True:
        # Calculate the triangular number for the current index
        triangular_number = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference between the triangular number and the target value
        difference = triangular_number - target_value
        
        # Check if the triangular number equals the target value
        if triangular_number == target_value:
            print(current_index)
            break
        
        # Check if the triangular number is greater than the target value
        if triangular_number > target_value:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(current_index)
                break
        
        # Increment the index to check the next triangular number
        current_index += 1

# Execute the function
find_triangular_index()
