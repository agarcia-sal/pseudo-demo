# Step 1: Read an integer input that represents the size of an array
size_of_array = int(input())

# Step 2: Create a boolean list initialized to True, indicating all positions are available
boolean_array = [True] * size_of_array

# Step 3: Initialize variables for loop control
current_position = 0  # This will track the current position in the boolean array
step_size = 1         # This will be used to determine the step size

# Step 4: Start a loop that continues while step_size is less than or equal to 500000
while step_size <= 500000:
    # Step 4a: If the current position in the boolean array is True, mark it as False
    if boolean_array[current_position]:
        boolean_array[current_position] = False

    # Step 4b: Increment the step size by 1
    step_size += 1

    # Step 4c: Update the current position using the step size while wrapping around the array
    current_position = (current_position + step_size) % size_of_array

# Step 5: Extract all positions in the boolean array that are still True
remaining_true_positions = [pos for pos in boolean_array if pos]

# Step 6: Check if there are no remaining True positions
if len(remaining_true_positions) == 0:
    print('YES')  # Indicate that all positions have been marked False
else:
    print('NO')   # Indicate that there are still True positions left
