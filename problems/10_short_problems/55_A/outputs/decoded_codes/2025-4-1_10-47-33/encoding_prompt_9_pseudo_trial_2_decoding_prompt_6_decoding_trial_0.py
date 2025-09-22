# Step 1: Receive input and assign it to a variable
list_size = int(input())

# Step 2: Initialize a boolean list with True values
boolean_list = [True] * list_size  # List of size `list_size`, all elements are True

# Step 3: Initialize iteration variables
current_index = 0
step = 1

# Step 4: Loop through specified iterations
while step <= 500000:
    # Step 5: Check the current position in boolean_list
    if boolean_list[current_index]:  # If the current position is True
        boolean_list[current_index] = False  # Set it to False

    # Increment the step and update the current index
    step += 1
    current_index = (current_index + step) % list_size  # Update position using modulo

# Step 6: Check remaining True values
remaining_true = [value for value in boolean_list if value]  # List of remaining True values

# Step 7: Output the result
if len(remaining_true) == 0:  # If no True values remain
    print("YES")
else:
    print("NO")  # Otherwise, print NO
