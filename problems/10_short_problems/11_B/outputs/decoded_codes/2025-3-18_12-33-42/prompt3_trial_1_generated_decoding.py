def find_triangle_number_index():
    # Step 2: Prompt user for input
    user_input = input()
    
    # Step 3: Store absolute value of the input
    input_value = abs(int(user_input))  # Convert input to integer and take absolute value

    # Step 4: Initialize index to 0
    index = 0

    # Step 5: Infinite loop to find the required index
    while True:
        # Step 5a: Calculate triangle number using the formula
        triangle_number = index * (index + 1) // 2  # Using integer division
        
        # Step 5b: Calculate the difference
        difference = triangle_number - input_value
        
        # Step 5c: Check if the triangle number equals inputValue
        if triangle_number == input_value:
            print(index)  # Output the index
            break  # Exit the loop
        
        # Step 5d: Check if the triangle number exceeds inputValue
        elif triangle_number > input_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break  # Exit the loop
        
        # Step 5e: Increment index by 1 for the next iteration
        index += 1

# You can call the function to execute it:
find_triangle_number_index()
