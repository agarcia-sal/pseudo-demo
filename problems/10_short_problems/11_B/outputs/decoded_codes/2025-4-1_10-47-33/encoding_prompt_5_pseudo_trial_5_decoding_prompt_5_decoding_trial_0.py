def find_triangular_number_index():
    # Read user input and convert to absolute value
    target_number = abs(int(input()))
    
    index = 0  # Initialize the counter for triangular numbers
    
    while True:
        # Calculate the triangular number using the formula n*(n+1)/2
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the target number
        difference = triangular_number - target_number
        
        # Check if the triangular number matches the target number
        if triangular_number == target_number:
            print(index)  # Found the exact match
            break
        # Check if the triangular number exceeds the target number
        elif triangular_number > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Found a valid index
                break
        
        index += 1  # Increment the index to check the next triangular number

# The function can be tested by calling it:
# find_triangular_number_index()
