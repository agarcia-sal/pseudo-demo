def find_smallest_integer():
    # Step 1: Get the absolute target sum from user input
    target_sum = abs(int(input()))
    
    # Step 2: Initialize a counter
    current_index = 0

    # Step 3: Loop for calculation
    while True:
        # Calculate the sum of the first current_index integers
        current_sum = (current_index * (current_index + 1)) // 2  # Integer division
        
        # Calculate the difference between current_sum and target_sum
        difference = current_sum - target_sum
        
        # Check conditions
        if current_sum == target_sum:
            print(current_index)
            return  # Stop the process
        
        if current_sum > target_sum:
            if difference % 2 == 0:  # Check if the difference is even
                print(current_index)
                return  # Stop the process
        
        # Increment current index by 1 for the next iteration
        current_index += 1

# Call the function to execute
find_smallest_integer()
