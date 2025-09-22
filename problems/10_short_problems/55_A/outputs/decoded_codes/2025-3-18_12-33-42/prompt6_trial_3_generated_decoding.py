# Step 1: Read an integer input representing the size of the array
size = int(input())  # size will be a positive integer

# Step 2: Initialize a boolean array of the specified size where all elements are initially True
is_active = [True] * size  # Create a boolean array of length size and set all elements to True

# Step 3: Initialize tracking variables
index = 0
counter = 1

# Step 4: Use a loop to iterate while counter is less than or equal to 500,000
while counter <= 500000:
    # Step 4a: If the current position in the is_active array is True
    if is_active[index]:
        # Step 4b: Mark the current position as False
        is_active[index] = False
    
    # Step 4c: Increment the counter for the next step
    counter += 1

    # Step 4d: Calculate the next index using the formula (index + counter) modulo size
    index = (index + counter) % size

# Step 5: Filter the is_active array to get a new list of True values
active_elements = [active for active in is_active if active]  # Create a list of all True elements from is_active

# Step 6: Check if there are any True values in the active_elements list
if len(active_elements) == 0:
    print('YES')  # Indicating no active elements are found
else:
    print('NO')   # Indicating at least one active element is found
