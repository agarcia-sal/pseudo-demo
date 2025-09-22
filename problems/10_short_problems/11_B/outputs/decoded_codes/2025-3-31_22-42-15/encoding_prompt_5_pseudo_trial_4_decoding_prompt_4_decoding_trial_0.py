def find_triangular_number():
    # Step 2: Get user input and store the absolute value
    target_value = abs(int(input()))

    # Step 3: Initialize the counter
    counter = 0

    # Step 4: Begin an endless loop to find the triangular number
    while True:
        # Step 4a: Calculate the triangular number
        triangular_number = (counter * (counter + 1)) // 2
        
        # Step 4b: Calculate the difference
        difference = triangular_number - target_value
        
        # Step 4c: Check for a direct match
        if triangular_number == target_value:
            print(counter)  # Found a match
            break  # Exit the loop
        
        # Step 4d: Check if the triangular number is greater than target_value
        elif triangular_number > target_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)  # Different condition met
                break  # Exit the loop
        
        # Step 4e: Increment the counter
        counter += 1

# Start the program
find_triangular_number()
