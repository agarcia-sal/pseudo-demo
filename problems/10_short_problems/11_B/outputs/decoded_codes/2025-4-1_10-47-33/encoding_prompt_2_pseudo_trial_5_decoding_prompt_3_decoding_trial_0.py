def find_smallest_integer():
    # Step 1: Receive an integer input and store its absolute value
    absolute_value = abs(int(input()))
    
    # Step 2: Initialize a variable to track the current integer
    index = 0
    
    # Step 3: Enter an infinite loop for evaluation
    while True:
        # Calculate the sum of the first `index` integers
        sum_of_integers = index * (index + 1) // 2
        
        # Calculate the difference between sum and absolute value
        difference = sum_of_integers - absolute_value
        
        # Step 4: Check if sum_of_integers equals absolute_value
        if sum_of_integers == absolute_value:
            print(index)
            break  # Exit the loop
        
        # Step 5: Check if sum_of_integers is greater than absolute_value
        if sum_of_integers > absolute_value:
            # Step 5.1: Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop
        
        # Increase index to evaluate the next integer
        index += 1
