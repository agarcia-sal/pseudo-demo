def find_index_for_target():
    # Step 2: Read an integer value from the user and take its absolute value
    target_number = abs(int(input()))
    
    # Step 3: Initialize index
    index = 0

    # Step 4: Begin an infinite loop
    while True:
        # Calculate currentSum using the formula for the sum of the first index natural numbers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference
        difference = current_sum - target_number
        
        # Step 5: Check conditions
        if current_sum == target_number:
            print(index)
            break  # Exit the loop
        elif current_sum > target_number:
            # Check if difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop

        # Step 6: Increment the index by 1
        index += 1

# Call the function to execute
find_index_for_target()
