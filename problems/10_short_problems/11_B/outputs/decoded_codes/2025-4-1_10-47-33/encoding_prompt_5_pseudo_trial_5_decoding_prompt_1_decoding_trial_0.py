def find_triangular_number_index():
    # Accept a number as input and convert it to a non-negative integer
    target_number = abs(int(input()))
    
    # Initialize counter
    index = 0
    
    # Infinite loop to calculate triangular numbers
    while True:
        # Calculate triangular number
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate difference
        difference = triangular_number - target_number
        
        # Check conditions
        if triangular_number == target_number:
            print(index)  # Print the result
            break  # Exit the loop
        elif triangular_number > target_number:
            if difference % 2 == 0:  # Check if the difference is even
                print(index)  # Print the result
                break  # Exit the loop
        
        # Increment counter
        index += 1

# Start the program
find_triangular_number_index()
