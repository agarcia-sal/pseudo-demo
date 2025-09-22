def find_smallest_non_negative_integer():
    # Step 1: Read the given integer value and take its absolute value
    target_value = abs(int(input()))
    
    # Step 2: Initialize the index
    index = 0
    
    # Step 3: Loop until we find the desired index
    while True:
        # Step 3a: Calculate the current sum using the formula for the sum of the first 'index' integers
        current_sum = (index * (index + 1)) // 2
        
        # Step 3b: Calculate the difference
        difference = current_sum - target_value
        
        # Step 3c: Check if current_sum is equal to target_value
        if current_sum == target_value:
            print(index)
            break
        
        # Step 3d: If current_sum is greater than target_value
        if current_sum > target_value:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 3e: Increment the index for the next iteration
        index += 1

# Call the function to initiate the process
find_smallest_non_negative_integer()
