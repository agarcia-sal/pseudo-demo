def find_triangle_number_index():
    # Step 1: Get user input and convert to a positive integer
    target_triangle_number = int(input())
    
    # Step 2: Initialize the index to track the current triangle number
    index = 0
    
    # Step 3: Begin an infinite loop for evaluating triangle numbers
    while True:
        # Step 3a: Calculate the triangle number for the current index
        triangle_number = (index * (index + 1)) // 2
        
        # Step 3b: Calculate the difference from the target triangle number
        difference = triangle_number - target_triangle_number
        
        # Step 3c: Check if triangle number matches the target
        if triangle_number == target_triangle_number:
            print(index)
            break  # Exit the loop if found
        
        # Step 3d: Check if triangle number exceeds target
        if triangle_number > target_triangle_number:
            # Step 3d.1: Determine if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop if condition met
        
        # Step 3e: Increment index for the next iteration
        index += 1

# Call the function to execute
find_triangle_number_index()
