def find_triangle_number():
    # Convert input to absolute integer
    n = abs(int(input()))  # Read input and take absolute integer
    i = 0  # Initialize counter for triangle number calculation

    # Infinite loop until a solution is found
    while True:
        # Calculate the triangle number for current i
        triangle_number = (i * (i + 1)) // 2  # Use integer division to calculate the triangle number
        difference = triangle_number - n  # Calculate the difference from input
        
        # Check if current triangle number equals input
        if triangle_number == n:
            print(i)  # Output the index of the triangle number
            break
        
        # Check if current triangle number exceeds input
        elif triangle_number > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(i)  # Output the index of the triangle number
                break
        
        # Increment to the next triangle number
        i += 1  # Move to the next value of i

# Call the function to execute
find_triangle_number()
