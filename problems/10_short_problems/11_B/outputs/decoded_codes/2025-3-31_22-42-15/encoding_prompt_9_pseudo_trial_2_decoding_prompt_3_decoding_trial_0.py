def find_smallest_triangular_adjustment():
    # Step 1: Receive Input
    targetNumber = abs(int(input()))  # Get an absolute integer input from the user.

    # Step 2: Initialize Variables
    currentInteger = 0  # Variable to keep track of the current integer being evaluated.

    # Step 3: Start an Infinite Loop
    while True:
        # Step 4: Calculate Triangular Number
        triangularNumber = (currentInteger * (currentInteger + 1)) // 2  # Use integer division.

        # Step 5: Determine the Difference
        difference = triangularNumber - targetNumber

        # Step 6: Check Conditions
        if triangularNumber == targetNumber:
            print(currentInteger)  # Output currentInteger if triangularNumber matches targetNumber.
            break  # Exit the loop (valid number found).

        elif triangularNumber > targetNumber:
            if difference % 2 == 0:  # Check if difference is an even number.
                print(currentInteger)  # Output currentInteger for valid adjustment.
                break  # Exit the loop (valid adjustment found).

        # Step 7: Increment the Integer
        currentInteger += 1  # Increase currentInteger by 1 for the next iteration.

# To execute the function
find_smallest_triangular_adjustment()
