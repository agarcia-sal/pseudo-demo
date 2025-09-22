def find_first_non_negative_integer():
    # Step 1: Initialize Input
    n = abs(int(input()))  # Get an absolute integer input value 'n' from the user

    # Step 2: Set Initial Values
    index = 0  # Initialize index to 0

    # Step 3: Repeat Until Found
    while True:  # Create an infinite loop
        # Step 4: Calculate Sum
        sum_up_to_index = (index * (index + 1)) // 2  # Calculate the sum using integer division

        # Step 5: Determine the Difference
        difference = sum_up_to_index - n  # Calculate the difference

        # Step 6: Check for Equality
        if sum_up_to_index == n:
            print(index)  # Output the current index
            break  # Exit the loop

        # Step 7: Check for Greater Than Condition
        if sum_up_to_index > n:
            if difference % 2 == 0:  # Check if the difference is even
                print(index)  # Output the current index
                break  # Exit the loop

        # Step 8: Increment Index
        index += 1  # Increase index by 1 to check the next integer

# Call the function to execute
find_first_non_negative_integer()
