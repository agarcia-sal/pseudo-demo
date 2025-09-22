# Function to find the triangular number solution for a given integer input
def triangular_number_solution():
    # Step 1: Initialize the variable
    n = abs(int(input()))  # Set n to the absolute value of the integer input
    i = 0  # Set i to 0, the counter for triangular numbers

    # Step 2: Start an infinite loop to calculate triangular numbers
    while True:
        # Step 3: Calculate the triangular number for the current i
        s = (i * (i + 1)) // 2  # Use integer division for triangular number calculation

        # Step 4: Calculate the difference between the triangular number and n
        m = s - n

        # Step 5: Check if the triangular number equals n
        if s == n:
            print(i)  # Print i if the triangular number is equal to n
            break

        # Step 6: Check if the triangular number exceeds n
        elif s > n:
            # Step 7: Check if the difference is even
            if m % 2 == 0:
                print(i)  # Print i if the difference is even
                break

        # Step 8: Increment i for the next iteration
        i += 1  # Increment i for the next triangular number

# Uncomment below to test the function
# triangular_number_solution()
