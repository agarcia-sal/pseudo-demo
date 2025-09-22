def find_smallest_integer():
    # Step 1: Get the absolute value of the user input
    target_number = abs(int(input()))
    
    # Step 2: Initialize the current integer to 0
    current_integer = 0
    
    # Step 3: Start an infinite loop to find the solution
    while True:
        # Calculate the sum of integers from 0 to current_integer
        sum_of_integers = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference
        difference = sum_of_integers - target_number
        
        # Check if the sum equals the target number
        if sum_of_integers == target_number:
            print(current_integer)
            break
        
        # Check if the sum exceeds the target number
        if sum_of_integers > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_integer)
                break
        
        # Increment current_integer by 1 for the next iteration
        current_integer += 1

# Call the function to execute
find_smallest_integer()
