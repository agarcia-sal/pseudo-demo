def find_triangular_number():
    # Read an integer input from the user
    n = abs(int(input()))  # Get the absolute value of the integer input
    i = 0  # Initialize counter i to 0

    while True:  # Start an infinite loop
        # Compute the triangular number s
        s = (i * (i + 1)) // 2  # Use integer division to compute the triangular number
        m = s - n  # Calculate the difference

        # Check the conditions
        if s == n:
            print(i)  # Display the value of i
            break  # Exit the loop
        elif s > n:
            if m % 2 == 0:  # Check if m is even
                print(i)  # Display the value of i
                break  # Exit the loop
            
        i += 1  # Increment i by 1

# Run the function to execute the logic
find_triangular_number()
