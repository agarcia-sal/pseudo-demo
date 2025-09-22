def find_integer_solution():
    # Step 1: Initialize Variables
    n = abs(int(input()))  # Get absolute value of input from user
    i = 0  # Initialize counter

    # Step 2: Start an Infinite Loop
    while True:
        # Step 3: Calculate Sum of first i integers
        s = (i * (i + 1)) // 2  # Use integer division for correctness

        # Step 4: Calculate Difference
        m = s - n  # Calculate the difference

        # Step 5: Check for Exact Match
        if s == n:
            print(i)
            break  # Exit the loop if exact match found

        # Step 6: Check for Overreach
        if s > n:
            if m % 2 == 0:  # Check if difference is even
                print(i)
                break  # Exit the loop if overreach is even

        # Step 7: Increment Counter
        i += 1  # Increase the counter

# Call the function to execute
find_integer_solution()
