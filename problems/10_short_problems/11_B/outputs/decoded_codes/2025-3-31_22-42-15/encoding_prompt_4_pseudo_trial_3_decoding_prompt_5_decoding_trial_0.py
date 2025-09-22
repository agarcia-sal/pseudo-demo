def find_triangle_number():
    # Read a number n from the user
    n = abs(int(input()))
    
    # Initialize the index for triangular numbers
    i = 0
    
    while True:
        # Calculate the triangular number for the current index i
        triangular_number = (i * (i + 1)) // 2
        difference = triangular_number - n
        
        # Check if the triangular number equals n
        if triangular_number == n:
            print(i)
            break
        
        # Check if the triangular number is greater than n
        elif triangular_number > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)
                break
        
        # Increment the index for the next triangular number
        i += 1
