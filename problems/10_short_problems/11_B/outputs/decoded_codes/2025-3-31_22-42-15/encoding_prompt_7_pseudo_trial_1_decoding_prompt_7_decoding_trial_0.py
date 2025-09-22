def find_triangle_number_position():
    # Step 1: Read the input number and convert it to an absolute integer
    input_number = int(input())
    absolute_value = abs(input_number)
    
    # Step 2: Initialize the index variable
    index = 0
    
    # Step 3: Loop indefinitely
    while True:
        # Step 4: Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2
        
        # Step 5: Calculate the difference between the triangular number and the absolute value
        difference = triangular_number - absolute_value
        
        # Step 6: Check if the triangular number matches the absolute value
        if triangular_number == absolute_value:
            print(index)  # Output the current index
            break  # Exit the loop if a match is found
            
        # Step 7: Check if the triangular number exceeds the absolute value
        elif triangular_number > absolute_value:
            # Step 8: Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop if the conditions are satisfied
                
        # Step 9: Increment the index for the next iteration
        index += 1
