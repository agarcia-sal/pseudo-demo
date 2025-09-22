def find_matching_number():
    # Step 1: Initialize Variables
    n = abs(int(input()))  # Get the absolute value of the user's input
    i = 0  # Initialize the counter

    # Step 2: Start Infinite Loop
    while True:
        # Step 2a: Calculate the Sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Use integer division for sum calculation

        # Step 2b: Calculate the Difference
        m = s - n

        # Step 2c: Check for Match
        if s == n:
            print(i)  # Print the value of i
            break  # Exit the loop

        # Step 2d: Check for Exceeding Value
        if s > n:
            if m % 2 == 0:  # Check if m is divisible by 2
                print(i)  # Print the value of i
                break  # Exit the loop

        # Step 2e: Increment Loop Counter
        i += 1  # Increase i by 1

# Call the function to execute
find_matching_number()
