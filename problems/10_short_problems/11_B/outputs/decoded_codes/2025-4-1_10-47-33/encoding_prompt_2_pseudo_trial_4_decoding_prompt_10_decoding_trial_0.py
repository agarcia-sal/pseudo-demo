def find_target_sum_index():
    # 2. Input: Read an integer from the user and store its absolute value
    target_sum = abs(int(input()))
    
    # 3. Initialize
    current_index = 0

    # 4. Loop: Begin an infinite loop
    while True:
        # 4.1 Calculate current sum using the formula for the sum of the first n integers
        current_sum = (current_index * (current_index + 1)) // 2
        
        # 4.2 Calculate difference from target
        difference_from_target = current_sum - target_sum
        
        # 4.3 Check for Exact Match
        if current_sum == target_sum:
            print(current_index)
            break  # Exit the loop

        # 4.4 Check for Exceeding Target
        if current_sum > target_sum:
            # If the difference is even, print the index and exit
            if difference_from_target % 2 == 0:
                print(current_index)
                break  # Exit the loop

        # 4.5 Increment
        current_index += 1

# Call the function to execute it
find_target_sum_index()
