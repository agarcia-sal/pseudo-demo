def find_largest_integer():
    # Step 1: Receive input and store the absolute value
    target_value = abs(int(input()))
    
    # Step 2: Initialize a counter
    counter = 0
    
    # Step 3: Begin an infinite loop
    while True:
        # Step 4: Calculate the sum of the first `counter` integers
        current_sum = counter * (counter + 1) // 2   # Use integer division
        
        # Step 5: Calculate the difference
        difference = current_sum - target_value
        
        # Step 6: Check for equality
        if current_sum == target_value:
            print(counter)  # Output the solution
            break
            
        # Step 7: Check exceedance condition
        if current_sum > target_value:
            if difference % 2 == 0:  # Check if difference is even
                print(counter)  # Output the solution
                break
        
        # Step 8: Increment counter
        counter += 1

# Call the function to execute the algorithm
find_largest_integer()
