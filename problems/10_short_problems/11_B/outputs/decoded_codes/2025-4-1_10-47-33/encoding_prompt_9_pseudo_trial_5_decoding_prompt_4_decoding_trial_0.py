def find_smallest_index():
    # Step 1: Receive and prepare input
    target_number = int(input())
    
    # Step 2: Initialize variables
    current_index = 0
    
    # Step 3: Process to find the desired index
    while True:
        # Calculate the triangular number
        triangular_number = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference
        difference = triangular_number - target_number
        
        # Check if triangular number equals target number
        if triangular_number == target_number:
            print(current_index)
            break
        
        # Check if triangular number exceeds target number
        elif triangular_number > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_index)
                break
        
        # Increment the index for the next iteration
        current_index += 1

# Call the function to execute the logic
find_smallest_index()
