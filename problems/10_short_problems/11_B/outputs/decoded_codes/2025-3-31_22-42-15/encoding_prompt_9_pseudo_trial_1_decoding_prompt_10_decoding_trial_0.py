def find_least_integer():
    # Step 1: Initialize the absolute value from user input
    absolute_value = abs(int(input()))
    index = 0  # This will be used to calculate triangular numbers

    # Start an infinite loop
    while True:
        # Step 2: Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2
        
        # Step 3: Calculate the difference between triangular number and absolute value
        difference = triangular_number - absolute_value
        
        # Step 4: Check if we found the correct triangular number
        if triangular_number == absolute_value:
            print(index)
            break
        
        # Step 5: Check if the triangular number is greater than absolute value
        if triangular_number > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 6: Increment index for the next triangular number
        index += 1

# Call the function to execute the program
find_least_integer()
