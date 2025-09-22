def find_smallest_triangular_index():
    # Step 1: Receive and prepare input
    target_number = int(input())
    
    # Step 2: Initialize variables
    current_index = 0
    
    while True:  # Step 3: Process to find the desired index
        # Calculate the triangular number
        triangular_number = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference
        difference = triangular_number - target_number
        
        # Check if we found an exact match
        if triangular_number == target_number:
            print(current_index)  # Print the index for an exact match
            break
        elif triangular_number > target_number:  # Check for exceedance
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_index)  # Print the index for an even difference
                break
        
        # Increment the index for the next iteration
        current_index += 1

# Call the function to execute the code
find_smallest_triangular_index()
