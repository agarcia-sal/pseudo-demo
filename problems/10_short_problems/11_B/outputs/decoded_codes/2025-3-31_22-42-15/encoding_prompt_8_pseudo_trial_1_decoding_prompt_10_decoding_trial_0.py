def find_smallest_triangular_index():
    # 1. Obtain a positive integer from the user
    target_value = abs(int(input()))  # Store the absolute value of the input integer

    current_index = 0  # 2. Initialize current index

    while True:  # 3. Begin an infinite loop to calculate triangular numbers
        # a. Calculate the triangular number for current_index
        triangular_number = (current_index * (current_index + 1)) // 2
        
        # b. Calculate the difference between the triangular number and target_value
        difference = triangular_number - target_value
        
        # c. Check if the triangular number equals target_value
        if triangular_number == target_value:
            print(current_index)  # Print the current index
            break  # Exit the loop
        
        # d. Check if the triangular number is greater than target_value
        if triangular_number > target_value:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(current_index)  # Print the current index
                break  # Exit the loop

        # e. Increment current_index by 1 to check the next triangular number
        current_index += 1

# Testing the function can be done by calling it
find_smallest_triangular_index()
