# Function to find and print a specific integer based on triangular numbers
def find_triangular_number():
    # Get the absolute value of the input integer
    n = abs(int(input()))
    i = 0  # Initialize the index i

    # Begin an infinite loop
    while True:
        # Compute the triangular number s
        s = (i * (i + 1)) // 2  
        m = s - n  # Calculate the difference m

        # Check the conditions
        if s == n:
            print(i)  # Display the value of i
            break  # Exit the loop
        elif s > n:
            if m % 2 == 0:  # If m is an even number
                print(i)  # Display the value of i
                break  # Exit the loop

        i += 1  # Increment i by 1

# Example of running the function
find_triangular_number()
