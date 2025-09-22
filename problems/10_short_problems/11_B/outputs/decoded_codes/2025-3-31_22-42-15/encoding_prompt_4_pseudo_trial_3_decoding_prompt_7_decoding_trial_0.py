def find_triangle_number():
    # Read a number n from user input and take the absolute value
    n = abs(int(input()))
    
    # Initialize index i
    i = 0

    # Infinite loop to calculate and check triangular numbers
    while True:
        # Calculate the triangular number for the current index i
        s = (i * (i + 1)) // 2  # Using integer division
        m = s - n  # Calculate the difference

        # Check if the triangular number equals n
        if s == n:
            print(i)  # If yes, print the index i
            break  # Exit the loop

        # Check if the triangular number is greater than n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)  # If even, print the index i
                break  # Exit the loop

        # Increment the index i for the next triangular number
        i += 1

# Example of running the function
# Uncomment the line below to run the function
# find_triangle_number()
