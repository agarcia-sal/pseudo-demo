# Start of the program

# Step 2: Read an integer value `n` from user input
n = int(input())

# Step 3: Create a list `is_active` of length `n`, where all elements are initialized to `True`
is_active = [True] * n

# Step 4: Initialize `current_index` to 0
current_index = 0

# Step 5: Initialize `increment` to 1
increment = 1

# Step 6: While `increment` is less than or equal to 500000
while increment <= 500000:
    # Step 6.1: If the element at `current_index` in the list `is_active` is `True`
    if is_active[current_index]:
        # Step 6.1.1: Set the element at `current_index` in the list `is_active` to `False`
        is_active[current_index] = False
    
    # Step 6.2: Increment `increment` by 1
    increment += 1
    
    # Step 6.3: Update `current_index`
    current_index = (current_index + increment) % n

# Step 7: Create a list `active_elements` that contains only the `True` values from `is_active`
active_elements = [value for value in is_active if value]

# Step 8: Check the length of `active_elements`
if len(active_elements) == 0:
    # Step 8.1: Output "YES" if there are no `True` values left
    print("YES")
else:
    # Step 9: Output "NO" if there are still `True` values
    print("NO")

# End of the program
