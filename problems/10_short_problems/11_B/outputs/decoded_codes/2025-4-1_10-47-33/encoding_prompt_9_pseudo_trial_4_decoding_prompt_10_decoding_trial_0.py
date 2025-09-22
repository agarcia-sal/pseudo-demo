def find_largest_sequential_sum_index():
    # Step 1: Receive input
    target_value = abs(int(input()))
    
    # Step 2: Initialize a counter
    counter = 0

    # Step 3: Begin an infinite loop
    while True:
        # Step 4: Calculate the sum of integers
        current_sum = counter * (counter + 1) // 2  # Using integer division
        
        # Step 5: Calculate the difference
        difference = current_sum - target_value
        
        # Step 6: Check equality
        if current_sum == target_value:
            print(counter)  # Output the solution
            break
        
        # Step 7: Check exceedance condition
        if current_sum > target_value:
            if difference % 2 == 0:  # Check if the difference is even
                print(counter)  # Output the solution
                break
        
        # Step 8: Increment counter
        counter += 1

# Call the function to execute the algorithm
find_largest_sequential_sum_index()
