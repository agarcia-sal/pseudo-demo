def find_index_for_target_number():
    # Step 1: Input
    user_input = int(input())
    target_number = abs(user_input)  # Calculate absolute value
    
    # Step 2: Initialize index
    index = 0

    # Step 3: Loop
    while True:
        # Step 3.1: Calculate current sum of first 'index' natural numbers
        current_sum = index * (index + 1) // 2
        
        # Step 3.2: Calculate difference
        difference = current_sum - target_number
        
        # Step 3.3: Check Conditions
        if current_sum == target_number:
            print(index)
            break
        elif current_sum > target_number:
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 3.4: Increment index
        index += 1

# Call the function to execute the logic
find_index_for_target_number()
