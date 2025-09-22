def find_triangular_number_index():
    # Read user input and convert to non-negative integer
    target_number = abs(int(input()))
    index = 0  # Initialize the index for triangular numbers

    while True:
        # Calculate current triangular number
        triangular_number = (index * (index + 1)) // 2
        # Calculate the difference between triangular number and target number
        difference = triangular_number - target_number
        
        # Check if we found the desired triangular number
        if triangular_number == target_number:
            print(index)  # Print the index
            break
        elif triangular_number > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the index
                break
        
        index += 1  # Increment index to calculate next triangular number

# Call the function to execute the program
find_triangular_number_index()
