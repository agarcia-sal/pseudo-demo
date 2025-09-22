def find_index_for_target_number():
    # Step 1: Get a number from the user and convert it to an absolute integer
    target_number = abs(int(input()))
    
    # Step 2: Initialize a counter variable
    index = 0

    # Step 3: Enter an infinite loop
    while True:
        # Calculate the sum of the first `index` natural numbers
        sum_of_first_index = (index * (index + 1)) // 2  # Using integer division
        
        # Calculate the difference from the target number
        difference = sum_of_first_index - target_number
        
        # Step 4: Check if sum equals the target number
        if sum_of_first_index == target_number:
            print(index)
            break
        
        # Step 5: Check if sum exceeds the target number
        if sum_of_first_index > target_number:
            if difference % 2 == 0:  # Check if the difference is even
                print(index)
                break
        
        # Step 6: Increment the counter variable
        index += 1

# Execute the function
find_index_for_target_number()
