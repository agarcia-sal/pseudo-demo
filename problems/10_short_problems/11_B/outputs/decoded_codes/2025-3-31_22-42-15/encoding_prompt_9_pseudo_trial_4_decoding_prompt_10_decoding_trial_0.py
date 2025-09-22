def find_smallest_integer():
    # Step 2: Get the absolute value of the integer input from the user
    absolute_value = abs(int(input()))
    
    current_index = 0  # Step 3: Initialize the current index

    while True:  # Step 4: Start an indefinite loop
        # Step 4.1: Calculate the sum of the first current_index natural numbers
        sum_of_numbers = (current_index * (current_index + 1)) // 2  # Using integer division for clarity

        # Step 4.2: Calculate the difference
        difference = sum_of_numbers - absolute_value

        # Step 4.3: Check if the sum equals the absolute value
        if sum_of_numbers == absolute_value:
            print(current_index)  # Step 4.3.1: Print current_index
            break  # Step 4.3.2: Exit the loop
        
        # Step 4.4: Check if the sum is greater than the absolute value
        if sum_of_numbers > absolute_value:
            # Step 4.4.1: Check if the difference is even
            if difference % 2 == 0:
                print(current_index)  # Step 4.4.1.1: Print current_index
                break  # Step 4.4.1.2: Exit the loop
        
        current_index += 1  # Step 4.5: Increment the current index

# Execute the function
find_smallest_integer()
