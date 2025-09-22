def find_triangular_number_index():
    # Read user input and convert to non-negative integer
    target_number = abs(int(input()))
    
    # Initialize counter for triangular numbers
    index = 0
    
    while True:
        # Calculate the triangular number
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference
        difference = triangular_number - target_number
        
        # Check for exact match
        if triangular_number == target_number:
            print(index)
            break
        # Check if the triangular number is greater and difference is even
        elif triangular_number > target_number:
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the counter to check the next triangular number
        index += 1

# To run the function, call it:
find_triangular_number_index()
