def find_integer_for_desired_sum():
    # Step 2: Get Input
    desired_sum = abs(int(input()))  # Convert input to absolute integer

    # Step 3: Initialize a Counter
    i = 0  # Counter to track the number of terms

    # Step 4: Loop Indefinitely
    while True:
        # Step 4.1: Calculate the sum of the first i integers
        sum_of_first_i = (i * (i + 1)) // 2  # Using integer division

        # Step 4.2: Determine the difference
        difference = sum_of_first_i - desired_sum

        # Step 4.3: Check Conditions
        if sum_of_first_i == desired_sum:
            print(i)  # Found the exact match
            break  # Exit the loop

        if sum_of_first_i > desired_sum:
            if difference % 2 == 0:  # Check if the difference is even
                print(i)  # Found a valid 'i' by removing an even number
                break  # Exit the loop

        # Step 4.4: Increment the Counter
        i += 1  # Move to the next integer

# Call the function to execute
find_integer_for_desired_sum()
