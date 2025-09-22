# Initialize the main function for the computation
def main():
    # Read input from the user and ensure it's a non-negative integer
    n = abs(int(input()))  # Set n to the absolute value of the input
    i = 0  # Initialize i to 0 to start summing from the first integer

    # Begin an infinite loop
    while True:
        # Calculate the sum of the first 'i' integers using the triangular number formula
        s = (i * (i + 1)) // 2  # Use integer division for clarity

        # Calculate the difference between the sum and n
        m = s - n

        # Check if the sum 's' is equal to 'n'
        if s == n:
            print(i)  # Output the value of 'i' and exit
            break  # Exit the loop

        # Check if the sum 's' is greater than 'n'
        elif s > n:
            # Check if the difference 'm' is even
            if m % 2 == 0:
                print(i)  # Output the value of 'i' and exit
                break  # Exit the loop
        
        # Increment 'i' for the next iteration
        i += 1

# Call the main function to execute the program
main()
