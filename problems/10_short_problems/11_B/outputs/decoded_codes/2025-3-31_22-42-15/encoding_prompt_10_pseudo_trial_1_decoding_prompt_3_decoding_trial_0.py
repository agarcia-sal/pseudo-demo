def find_triangular_index():
    # Step 2: Read input and initialize variables
    n = abs(int(input()))  # Take input and get its absolute value
    i = 0  # Starting index

    # Step 3: Infinite loop to find the triangular number
    while True:
        # Calculate the triangular number
        s = (i * (i + 1)) // 2  # Using integer division for triangular number
        
        # Compute the difference
        m = s - n

        # Step 4: Check the conditions
        if s == n:
            print(i)  # Found the exact triangular number
            break  # Exit the loop
        elif s > n:
            if m % 2 == 0:
                print(i)  # Found the triangular number with even difference
                break  # Exit the loop
        
        # Step 5: Increment the index
        i += 1

# Call the function to execute the logic
find_triangular_index()
