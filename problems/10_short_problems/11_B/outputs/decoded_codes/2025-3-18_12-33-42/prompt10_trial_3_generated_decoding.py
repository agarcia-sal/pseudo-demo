def find_matching_i():
    # Step 1: Initialize Variables
    n = abs(int(input()))  # Get absolute value of the user input
    i = 0  # Initialize counter

    # Step 2: Start an Infinite Loop
    while True:
        # Step 3a: Calculate Sum
        s = (i * (i + 1)) // 2  # Using the arithmetic sum formula

        # Step 3b: Calculate Difference
        m = s - n

        # Step 3c: Check for Matches
        if s == n:
            print(i)
            break  # Exit the loop if sum matches n

        # Step 3d: Check for Greater Sum
        elif s > n:
            if m % 2 == 0:  # If the difference is even
                print(i)
                break  # Exit the loop if the condition is met

        # Step 3e: Increment the Counter
        i += 1  # Increase the value of i by 1

# Calling the function to execute
find_matching_i()
