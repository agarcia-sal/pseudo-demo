def find_triangle_number():
    # Read a number n from user input
    n = abs(int(input()))  # Convert input to integer and take absolute value

    i = 0  # Initialize index for triangular number calculation

    while True:
        # Calculate the triangular number for index i
        triangular_number = (i * (i + 1)) // 2
        difference = triangular_number - n
        
        # Check if the triangular number is equal to n
        if triangular_number == n:
            print(i)
            break
        
        # Check if the triangular number exceeds n
        elif triangular_number > n:
            # Verify if the difference is even
            if difference % 2 == 0:
                print(i)
                break
        
        # Move to the next index
        i += 1
