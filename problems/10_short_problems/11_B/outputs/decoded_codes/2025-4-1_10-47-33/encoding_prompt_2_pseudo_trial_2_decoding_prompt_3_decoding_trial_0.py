def find_triangle_number_index():
    # Step 1: Take input from user and convert it to a positive integer
    target_triangle_number = int(input())
    
    # Step 2: Initialize index to zero
    index = 0
    
    # Step 3: Infinite loop to evaluate potential triangle numbers
    while True:
        # a. Calculate the triangle number for the current index
        triangle_number = (index * (index + 1)) // 2  # using // for integer division
        
        # b. Compute the difference
        difference = triangle_number - target_triangle_number
        
        # c. Check if triangle number is equal to the targetTriangleNumber
        if triangle_number == target_triangle_number:
            print(index)  # Output the index
            break  # Terminate the loop
        
        # d. Check if the triangle number exceeds the targetTriangleNumber
        if triangle_number > target_triangle_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break  # Terminate the loop
        
        # e. Increment the index for the next iteration
        index += 1

# Call the function to execute
find_triangle_number_index()
