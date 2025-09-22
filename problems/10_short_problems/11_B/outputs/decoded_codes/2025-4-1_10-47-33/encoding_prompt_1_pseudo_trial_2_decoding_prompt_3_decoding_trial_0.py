def calculate_max_integer():
    # Step 1: Input Handling
    absolute_input = abs(int(input()))

    # Step 2: Initialize a Counter
    index = 0
    
    # Step 3: Infinite Loop for Calculation
    while True:
        # Step 3.1: Calculate currentSum using the formula
        current_sum = (index * (index + 1)) // 2
        
        # Step 3.2: Calculate the difference
        difference = current_sum - absolute_input
        
        # Step 3.3: Check Conditions
        if current_sum == absolute_input:
            print(index)
            break
        elif current_sum > absolute_input:
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 3.4: Increment the Counter
        index += 1

# Call the function to execute the program
calculate_max_integer()
