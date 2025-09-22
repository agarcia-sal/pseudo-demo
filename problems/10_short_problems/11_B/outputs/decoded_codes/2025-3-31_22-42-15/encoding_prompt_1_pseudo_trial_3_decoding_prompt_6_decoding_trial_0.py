# Step 1: Receive Input
target_value = abs(int(input()))  # Read an integer input and store its absolute value

# Step 2: Initialize Counter
index = 0  # Start with index at 0

# Step 3: Infinite Loop: Continue until the specified conditions are met
while True:
    # Step 4: Calculate Triangle Number
    triangular_number = (index * (index + 1)) // 2  # Calculate the triangular number using integer division

    # Step 5: Calculate Difference
    difference = triangular_number - target_value  # Determine the difference

    # Step 6: Check Conditions
    if triangular_number == target_value:  # Condition to check if the triangular number matches target value
        print(index)  # Output the current index
        break  # Exit the loop

    elif triangular_number > target_value:  # Condition when triangular number exceeds target value
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Output the current index
            break  # Exit the loop

    # Step 7: Increment Counter
    index += 1  # Increase index by 1 for the next iteration
