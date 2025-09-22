def find_triangular_number_index():
    # Read user input and convert it to an absolute value
    target_number = abs(int(input()))  # Ensure the input is cast to an integer

    # Initialize the index for triangular numbers
    index = 0
    
    # Infinite loop to calculate triangular numbers
    while True:
        # Calculate the triangular number using the formula n*(n+1)/2
        triangular_number = (index * (index + 1)) // 2  # Use integer division
        
        # Calculate the difference between the triangular number and the target number
        difference = triangular_number - target_number
        
        # Check if we found the exact match
        if triangular_number == target_number:
            print(index)  # Output the index
            break  # Exit the loop
        
        # Check if the triangular number is greater than the target number
        elif triangular_number > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break  # Exit the loop
        
        # Increment the index to check the next triangular number
        index += 1

# Call the function to execute the program
find_triangular_number_index()
