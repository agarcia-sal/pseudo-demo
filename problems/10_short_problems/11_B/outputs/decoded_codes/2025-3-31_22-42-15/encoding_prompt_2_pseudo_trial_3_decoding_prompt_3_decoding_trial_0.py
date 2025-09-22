def find_smallest_integer():
    # Step 1: Input
    target_value = abs(int(input()))  # Taking the absolute value of the input

    # Step 2: Initialization
    index = 0  # This will hold the current index or integer we're summing up to
    
    # Step 3: Loop
    while True:
        # Step 3a: Calculate currentSum
        current_sum = (index * (index + 1)) // 2  # Sum of first `index` integers
        
        # Step 3b: Calculate the difference
        difference = current_sum - target_value
        
        # Step 3c: Check if currentSum is equal to targetValue
        if current_sum == target_value:
            print(index)
            break
        
        # Step 3d: Check if currentSum is greater than targetValue
        if current_sum > target_value:
            if difference % 2 == 0:  # Check if the difference is even
                print(index)
                break
        
        # Step 3e: Increment index for the next iteration
        index += 1

# Uncomment the line below to run the function
# find_smallest_integer()
