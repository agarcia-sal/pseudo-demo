# Step 1: Input - Read the size of the array from the user
array_size = int(input())

# Step 2: Initialize a boolean array of size n with all elements set to True
is_true = [True] * array_size

# Step 3: Set initial variables
current_index = 0
increment = 1

# Step 4: Loop while increment is less than or equal to 500000
while increment <= 500000:
    # Check if the current index has been processed
    if is_true[current_index]:
        # Mark the current index as processed (set to False)
        is_true[current_index] = False
    
    # Increment the increment value
    increment += 1
    
    # Update current index (with wrapping)
    current_index = (current_index + increment) % array_size

# Step 5: Check results - Create a list of remaining True values
remaining_true = [value for value in is_true if value]

# Step 6: Output results
if len(remaining_true) == 0:
    print("YES")  # All elements processed
else:
    print("NO")   # There are elements that remain True
