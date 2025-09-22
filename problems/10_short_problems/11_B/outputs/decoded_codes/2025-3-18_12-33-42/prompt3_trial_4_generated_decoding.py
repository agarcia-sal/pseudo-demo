def find_triangular_number():
    # Step 1: Read input and store its absolute value as an integer
    input_value = abs(int(input()))

    # Step 2: Initialize a counter variable
    index = 0

    # Step 3: Begin an infinite loop to calculate triangular numbers
    while True:
        # Step 4: Calculate the triangular number using the formula
        triangular_number = (index * (index + 1)) // 2
        
        # Step 5: Calculate the difference between the triangular number and input value
        difference = triangular_number - input_value
        
        # Step 6: Check if the triangular number is equal to the input value
        if triangular_number == input_value:
            # Step 6a: If equal, print the current index and exit the loop
            print(index)
            break
        
        # Step 7: Check if the triangular number exceeds the input value
        elif triangular_number > input_value:
            # Step 7a: Check if the difference is even
            if difference % 2 == 0:
                # Step 7b: If the difference is even, print the current index and exit the loop
                print(index)
                break
        
        # Step 8: Increment the index for the next iteration
        index += 1

# Call the function
find_triangular_number()
