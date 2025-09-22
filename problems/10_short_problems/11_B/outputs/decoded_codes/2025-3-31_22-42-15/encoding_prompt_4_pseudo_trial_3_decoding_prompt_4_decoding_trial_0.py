def find_triangle_number():
    # Read an integer input from the user and take its absolute value
    n = abs(int(input()))
    
    i = 0  # Initialize the index for triangular numbers
    
    while True:
        # Calculate the triangular number for the current index i
        s = (i * (i + 1)) // 2  # Use integer division to get the triangular number
        m = s - n  # Difference between the triangular number and n
        
        # Check if the triangular number equals n
        if s == n:
            print(i)  # Output the index i
            break  # Exit the loop
        
        # If the triangular number is greater than n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Output the index i
                break  # Exit the loop
        
        # Increment the index for the next triangular number
        i += 1

# Example of calling the function (you can uncomment the line below to test)
# find_triangle_number()
