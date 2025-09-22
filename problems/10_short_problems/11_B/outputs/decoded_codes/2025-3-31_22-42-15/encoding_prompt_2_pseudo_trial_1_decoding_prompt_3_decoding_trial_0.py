def find_index_for_target_number():
    # Step 1: Get a number from the user and convert it to an absolute integer.
    target_number = abs(int(input()))
    
    # Step 2: Initialize the index counter.
    index = 0
    
    # Step 3: Start an infinite loop.
    while True:
        # Calculate the sum of the first `index` natural numbers.
        sum_of_first_index = (index * (index + 1)) // 2
        
        # Step 4: Calculate the difference from the target number.
        difference = sum_of_first_index - target_number
        
        # Check if the current sum equals the target number.
        if sum_of_first_index == target_number:
            print(index)  # Print the index if it matches the target number.
            break
        
        # Step 5: Check if the current sum exceeds the target number.
        if sum_of_first_index > target_number:
            # Check if the difference is even.
            if difference % 2 == 0:
                print(index)  # Print the index if the difference is even.
                break
        
        # Step 6: Increment the index for the next iteration of the loop.
        index += 1

# Call the function to execute.
find_index_for_target_number()
