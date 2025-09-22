def find_smallest_triangular_index():
    # Step 1: Receive and prepare input
    target_number = int(input())  # Convert input to non-negative integer

    # Step 2: Initialize variables
    current_index = 0

    # Step 3: Process to find the desired index
    while True:
        # Calculate the triangular number
        triangular_number = (current_index * (current_index + 1)) // 2
        # Calculate the difference
        difference = triangular_number - target_number
        
        # Check if the triangular number is equal to the target number
        if triangular_number == target_number:
            print(current_index)  # This is the answer
            break
        
        # Check if the triangular number is greater than the target number
        if triangular_number > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_index)  # This is the answer
                break
            
        # Increment current index
        current_index += 1

# Call the function to execute
find_smallest_triangular_index()
