def find_target_index():
    # Step 1: Read an integer value from the user and take its absolute value.
    target_number = abs(int(input()))
    
    # Step 2: Initialize currentIndex to 0.
    current_index = 0
    
    while True:  # Step 3: Enter an infinite loop
        # Step 4: Calculate the sum of the first currentIndex natural numbers.
        current_sum = current_index * (current_index + 1) // 2  # Using the formula for the sum of the first n natural numbers
        
        # Step 5: Determine the difference between currentSum and targetNumber.
        difference = current_sum - target_number
        
        # Step 6: Check the condition for currentSum and targetNumber.
        if current_sum == target_number:
            print(current_index)  # If equal, display currentIndex
            break  # Exit the loop
        elif current_sum > target_number:
            if difference % 2 == 0:  # Check if difference is even
                print(current_index)  # If even, display currentIndex
                break  # Exit the loop
        
        # Step 7: Increment currentIndex by 1.
        current_index += 1

# Run the function to execute the program
find_target_index()
