def find_smallest_index():
    # Step 1: Get User Input
    target_number = abs(int(input()))
    
    # Step 2: Initialize Counter
    current_index = 0
    
    # Step 3: Loop Until a Condition is Met
    while True:
        # a. Calculate the sum of all integers from 0 to current_index
        current_sum = (current_index * (current_index + 1)) // 2  # Using the formula for the sum of the first n integers
        
        # b. Calculate the difference
        difference = current_sum - target_number
        
        # c. Check Conditions
        if current_sum == target_number:
            print(current_index)  # Found the answer
            break
        
        if current_sum > target_number:
            if difference % 2 == 0:
                print(current_index)  # Found the answer
                break
        
        # d. Increment current_index by 1
        current_index += 1

# Call the function to execute the program
find_smallest_index()
