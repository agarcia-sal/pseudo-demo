def find_triangular_number_index():
    # Read input and take the absolute value
    number = abs(int(input()))
    
    # Initialize index for triangular numbers
    index = 0

    # Infinite loop to find the solution
    while True:
        # Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference to check conditions
        difference = triangular_number - number
        
        # Check if the triangular number equals the input number
        if triangular_number == number:
            print(index)
            break
        
        # Check if the triangular number exceeds the input number
        elif triangular_number > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next triangular number
        index += 1

# To execute the function, uncomment the line below
# find_triangular_number_index()
