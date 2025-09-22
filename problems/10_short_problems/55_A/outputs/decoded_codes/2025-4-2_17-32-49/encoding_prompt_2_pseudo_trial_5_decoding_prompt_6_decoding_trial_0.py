# Start of the program

# Step 2: Read an integer value as totalElements
total_elements = int(input())

# Step 3: Initialize the isActive list and other variables
is_active = [True] * total_elements  # Create a list of True values
index = 0  # Initialize the index variable
step = 1   # Initialize the step variable

# Step 4: Loop while the step is less than or equal to 500,000
while step <= 500000:
    # Check if the current index in isActive is True
    if is_active[index]:
        is_active[index] = False  # Mark the element as inactive
    
    # Increment the step by 1
    step += 1
    
    # Update the index with the current step and wrap around using modulo
    index = (index + step) % total_elements

# Step 5: Filter active elements
active_elements = [element for element in is_active if element]

# Step 6: Check if no elements are active and print the appropriate message
if len(active_elements) == 0:
    print("YES")  # All elements are inactive
else:
    print("NO")   # Some elements are still active

# End of the program
