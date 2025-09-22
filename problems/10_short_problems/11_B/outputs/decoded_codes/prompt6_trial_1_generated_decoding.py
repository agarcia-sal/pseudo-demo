# Step 1: Initialize an integer variable 'absolute_value' with the absolute value of user input
absolute_value = abs(int(input()))

# Step 2: Initialize a counter variable 'current_index' to 0
current_index = 0

# Step 3: Start an indefinite loop
while True:
    # Step 3a: Calculate the sum 'sum_of_integers' using the triangular number formula
    sum_of_integers = (current_index * (current_index + 1)) // 2
    
    # Step 3b: Calculate the 'difference'
    difference = sum_of_integers - absolute_value

    # Step 3c: Check if 'sum_of_integers' equals 'absolute_value'
    if sum_of_integers == absolute_value:
        print(current_index)  # Output the result
        break  # Exit the loop

    # Step 3d: Check if 'sum_of_integers' is greater than 'absolute_value'
    elif sum_of_integers > absolute_value:
        # Step 3d.i: Check if 'difference' is even
        if difference % 2 == 0:
            print(current_index)  # Output the result
            break  # Exit the loop

    # Step 3e: Increment 'current_index'
    current_index += 1
