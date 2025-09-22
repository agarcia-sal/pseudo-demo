def find_triangular_number():
    # Step 1: Initialize the variable
    n = abs(int(input()))  # Read an absolute integer input
    i = 0  # Iterator for triangular numbers

    # Step 2: Start an infinite loop to calculate triangular numbers
    while True:
        # Step 3: Calculate the triangular number for the current i
        triangular_number = (i * (i + 1)) // 2  # Using integer division
        
        # Step 4: Calculate the difference between the triangular number and n
        difference = triangular_number - n

        # Step 5: Check if the triangular number equals n
        if triangular_number == n:
            print(i)  # Step 6: Output the index i
            break

        # Step 7: Check if the triangular number exceeds n
        elif triangular_number > n:
            # Step 8: Check if the difference is even
            if difference % 2 == 0:
                print(i)  # Output the index i
                break
        
        # Step 9: Increment i for the next iteration
        i += 1

# Call the function to execute
find_triangular_number()
