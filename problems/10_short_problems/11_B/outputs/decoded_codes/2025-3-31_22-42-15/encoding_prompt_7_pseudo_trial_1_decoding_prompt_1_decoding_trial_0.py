def find_triangle_number_position(input_number):
    # Step 1: Convert input to absolute integer
    absolute_value = abs(int(input_number))  # Ensure input is treated as an integer

    # Step 2: Initialize index variable
    index = 0
    
    # Step 3: Loop indefinitely
    while True:
        # Step 4: Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2  # Integer division

        # Step 5: Calculate the difference between the triangular number and the input number
        difference = triangular_number - absolute_value
        
        # Step 6: Check if the triangular number matches the input number
        if triangular_number == absolute_value:
            print(index)
            break  # Exit the loop if a match is found
            
        # Step 7: Check if the triangular number exceeds the input number
        elif triangular_number > absolute_value:
            # Step 8: Check if the difference is even
            if difference % 2 == 0:  # Check if the difference is even
                print(index)
                break  # Exit the loop if conditions are satisfied
        
        # Step 9: Increment index for the next iteration
        index += 1

# Example of calling the function; Uncomment the line below to test
# find_triangle_number_position(input())
