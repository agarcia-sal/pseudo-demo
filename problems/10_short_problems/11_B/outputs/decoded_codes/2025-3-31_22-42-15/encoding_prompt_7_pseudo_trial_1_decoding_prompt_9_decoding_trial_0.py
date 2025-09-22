def find_triangle_number_position():
    # Step 1: Read input from the user and convert it to an absolute integer
    input_number = int(input())
    absolute_value = abs(input_number)

    # Step 2: Initialize index variable
    index = 0

    # Step 3: Loop indefinitely
    while True:
        # Step 4: Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2  # Use integer division
        
        # Step 5: Calculate the difference between the triangular number and the absolute input number
        difference = triangular_number - absolute_value
        
        # Step 6: Check if the triangular number matches the absolute input number
        if triangular_number == absolute_value:
            print(index)  # Print the index if a match is found
            break  # Exit the loop

        # Step 7: Check if the triangular number exceeds the absolute input number
        elif triangular_number > absolute_value:
            # Step 8: Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the index if the conditions are satisfied
                break  # Exit the loop
        
        # Step 9: Increment index for the next iteration
        index += 1
