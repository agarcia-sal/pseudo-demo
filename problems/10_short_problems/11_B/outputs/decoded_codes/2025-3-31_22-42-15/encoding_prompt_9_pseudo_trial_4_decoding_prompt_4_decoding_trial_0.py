def find_smallest_integer():
    # Step 2: Get the absolute value of the input integer
    absolute_value = abs(int(input()))
    
    # Step 3: Initialize the current index
    current_index = 0
    
    # Step 4: Start the indefinite loop
    while True:
        # Step 4.1: Calculate the sum of the first current_index natural numbers
        sum_of_numbers = (current_index * (current_index + 1)) // 2
        
        # Step 4.2: Calculate the difference
        difference = sum_of_numbers - absolute_value
        
        # Step 4.3: Check if the sum equals the absolute value
        if sum_of_numbers == absolute_value:
            print(current_index)
            break
        
        # Step 4.4: Check if the sum exceeds the absolute value
        elif sum_of_numbers > absolute_value:
            # Step 4.4.1: Check if the difference is even
            if difference % 2 == 0:
                print(current_index)
                break
        
        # Step 4.5: Increment current index by 1
        current_index += 1

# Call the function to execute the algorithm
find_smallest_integer()
