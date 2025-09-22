# Step 1: Get the number of elements from user input
number_of_elements = int(input())

# Step 2: Create a list initialized with True values of size number_of_elements
is_active = [True] * number_of_elements

# Step 3: Initialize variables index and step
index = 0
step = 1

# Step 4: While step is less than or equal to 500000
while step <= 500000:
    # Step 4a: Check if the current index is True
    if is_active[index]:
        # Mark the index as inactive
        is_active[index] = False
    
    # Step 4b: Increment step by 1
    step += 1
    
    # Step 4c: Update index to (current index + step) % number_of_elements
    index = (index + step) % number_of_elements

# Step 5: Create a list of active elements that are still True
active_elements = [val for val in is_active if val]

# Step 6: Check if there are any active elements remaining
if len(active_elements) == 0:
    # Step 6a: If no active elements, print 'YES'
    print('YES')
else:
    # Step 6b: If there are active elements, print 'NO'
    print('NO')
