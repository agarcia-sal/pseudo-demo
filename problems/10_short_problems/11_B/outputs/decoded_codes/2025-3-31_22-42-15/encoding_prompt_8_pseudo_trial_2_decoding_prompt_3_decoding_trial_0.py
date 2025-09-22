def find_triangular_integer():
    # Get input from the user and convert it to an absolute integer
    absolute_input = abs(int(input()))
    
    # Initialize the counter for current integer
    current_integer = 0
    
    while True:
        # Calculate the triangular number for the current integer
        triangular_number = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference between the triangular number and the absolute input
        difference = triangular_number - absolute_input
        
        # Check if the triangular number is equal to the absolute input
        if triangular_number == absolute_input:
            print(current_integer)
            break
            
        # Check if the triangular number is greater than the absolute input
        elif triangular_number > absolute_input:
            # If the difference is even, print current_integer and stop
            if difference % 2 == 0:
                print(current_integer)
                break
        
        # Increment the current integer for the next iteration
        current_integer += 1

# Example usage: Uncomment the next line to run the function
# find_triangular_integer()
