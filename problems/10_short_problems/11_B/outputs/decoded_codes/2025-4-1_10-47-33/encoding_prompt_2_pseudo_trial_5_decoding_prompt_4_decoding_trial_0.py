def find_smallest_integer():
    # Step 1: Receive input and store its absolute value
    absolute_value = abs(int(input()))
    
    # Step 2: Initialize index to track current integer being evaluated
    index = 0
    
    while True:
        # Step 3: Calculate the sum of the first index integers
        sum_of_integers = index * (index + 1) // 2
        
        # Step 4: Calculate the difference between sum and absolute value
        difference = sum_of_integers - absolute_value
        
        # Step 5: Check the first condition: sum equals absolute value
        if sum_of_integers == absolute_value:
            print(index)
            break
        
        # Step 6: Check the second condition: sum exceeds absolute value
        if sum_of_integers > absolute_value:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next evaluation
        index += 1

# Calling the function to execute
find_smallest_integer()
