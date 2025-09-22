def find_triangle_number_index():
    # Step 1: Get user input and convert it to a positive integer
    target_triangle_number = int(input())
    
    # Step 2: Initialize the index variable
    index = 0
    
    # Step 3: Infinite loop to evaluate potential triangle numbers
    while True:
        # Step 3a: Calculate the triangle number
        triangle_number = (index * (index + 1)) // 2
        
        # Step 3b: Compute the difference
        difference = triangle_number - target_triangle_number
        
        # Step 3c: Check if triangle_number equals target_triangle_number
        if triangle_number == target_triangle_number:
            print(index)
            break
        
        # Step 3d: Check if triangle_number exceeds target_triangle_number
        if triangle_number > target_triangle_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 3e: Increment the index
        index += 1

# Call the function to execute the program
find_triangle_number_index()
