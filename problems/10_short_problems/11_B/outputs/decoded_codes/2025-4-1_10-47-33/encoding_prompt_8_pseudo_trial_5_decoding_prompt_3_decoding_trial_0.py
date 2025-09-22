def find_triangular_number():
    # Capture user input and convert it to a non-negative integer
    input_value = abs(int(input()))
    
    # Initialize a counter for the current index
    current_index = 0

    # Infinite loop for calculation
    while True:
        # Calculate the triangular number
        triangular_sum = (current_index * (current_index + 1)) // 2

        # Determine the difference
        difference = triangular_sum - input_value

        # Check for exact match
        if triangular_sum == input_value:
            print(current_index)  # Output the current index
            break  # Exit the loop

        # Check if triangular sum exceeds input value
        if triangular_sum > input_value:
            if difference % 2 == 0:  # Check if the difference is even
                print(current_index)  # Output the current index
                break  # Exit the loop

        # Increment the counter
        current_index += 1

# Call the function to execute
find_triangular_number()
