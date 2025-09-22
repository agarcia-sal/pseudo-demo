def find_triangle_number_index():
    # Get the absolute value of the user input as an integer
    input_value = abs(int(input()))
    
    # Initialize the index variable
    index = 0
    
    # Infinite loop to find the triangle number index
    while True:
        # Calculate the ith triangle number using the formula
        triangle_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangle number and the input value
        difference = triangle_number - input_value
        
        # Check if the triangle number equals the input value
        if triangle_number == input_value:
            # Print the index if a match is found
            print(index)
            break  # Exit the loop
            
        # If the triangle number exceeds the input value
        elif triangle_number > input_value:
            # Check if the difference is even
            if difference % 2 == 0:
                # Print the index if the difference is even
                print(index)
                break  # Exit the loop
                
        # Increment the index for the next iteration
        index += 1

# You can call the function to test it
# find_triangle_number_index()
