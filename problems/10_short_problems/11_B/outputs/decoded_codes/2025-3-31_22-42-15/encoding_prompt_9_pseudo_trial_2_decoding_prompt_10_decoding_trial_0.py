def find_smallest_triangular_integer():
    # Step 1: Receive Input
    target_number = abs(int(input())) # Convert input to absolute integer value

    # Step 2: Initialize Variables
    current_integer = 0

    # Step 3: Start an Infinite Loop
    while True:
        # Step 4: Calculate Triangular Number
        triangular_number = (current_integer * (current_integer + 1)) // 2  # Use integer division
        
        # Step 5: Determine the Difference
        difference = triangular_number - target_number
        
        # Step 6: Check Conditions
        if triangular_number == target_number:
            print(current_integer)  # Output the current integer if it's exact match
            break  # Exit the loop (valid number found)
        
        elif triangular_number > target_number:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(current_integer)  # Output current integer if valid adjustment found
                break  # Exit the loop
        
        # Step 7: Increment the Integer
        current_integer += 1

# Invoke the function
find_smallest_triangular_integer()
