def calculate_max_integer():
    # Step 1: Input Handling
    absolute_input = abs(int(input()))  # Read a number from the user and store its absolute value

    # Step 2: Initialize a Counter
    index = 0  # Variable to keep track of the current integer

    # Step 3: Infinite Loop for Calculation
    while True:
        # Calculate the sum of the first `index` integers
        current_sum = (index * (index + 1)) // 2  # Use integer division
        
        # Calculate the difference between `current_sum` and `absolute_input`
        difference = current_sum - absolute_input

        # Step 3.3: Check Conditions
        if current_sum == absolute_input:
            print(index)  # Output the value of index as the result
            break  # Exit the loop

        if current_sum > absolute_input:
            if difference % 2 == 0:  # Check if difference is an even number
                print(index)  # Output the value of index as the result
                break  # Exit the loop
        
        # Step 3.4: Increment the Counter
        index += 1  # Increase index to consider the next integer


# End of Program
calculate_max_integer()
