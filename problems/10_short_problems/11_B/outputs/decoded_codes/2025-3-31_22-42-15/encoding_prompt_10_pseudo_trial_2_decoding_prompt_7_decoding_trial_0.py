# Function to find the smallest triangular number index satisfying specific conditions
def find_triangular_number_index():
    # Step 1: Initialize the variable
    n = abs(int(input()))  # Read integer input and take its absolute value
    i = 0  # Initialize an iterator for triangular numbers

    # Step 2: Start an infinite loop to calculate triangular numbers
    while True:
        # Step 3: Calculate the triangular number for the current i
        s = (i * (i + 1)) // 2  # Using integer division to compute triangular number
        
        # Step 4: Calculate the difference between the triangular number and n
        m = s - n  # Difference between triangular number and input

        # Step 5: Check if the triangular number equals n
        if s == n:  # Check for equality
            print(i)  # Print the index
            break  # Exit the loop

        # Step 6: Check if the triangular number exceeds n
        elif s > n:  # When triangular number is greater than input
            # Step 7: Check if the difference is even
            if m % 2 == 0:  # Check if difference is even
                print(i)  # Print the index
                break  # Exit the loop

        # Step 8: Increment i for the next iteration
        i += 1  # Prepare for the next triangular number calculation


# Call the function to execute
find_triangular_number_index()
