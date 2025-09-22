def find_triangle_number():
    # Read a number from user input
    n = int(input())  # Convert input to an integer
    n = abs(n)  # Get the absolute value of n

    i = 0  # Initialize the index for triangular numbers
    while True:  # Infinite loop until we find a suitable triangular number
        # Calculate the triangular number for index i
        s = (i * (i + 1)) // 2
        m = s - n  # Calculate difference to check conditions

        # Check if the current triangular number equals n
        if s == n:
            print(i)  # Print the index i
            break  # Exit the loop
        
        # Check if the triangular number exceeds n
        elif s > n:
            # If the difference m is even
            if m % 2 == 0:
                print(i)  # Print the index i
                break  # Exit the loop

        i += 1  # Increment index i for the next triangular number

# To call the function, uncomment the line below:
# find_triangle_number()
