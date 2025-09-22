# Step 1: Read an integer value n which represents the number of elements.
number_of_elements = int(input())

# Step 2: Initialize the list and other variables
is_true = [True] * number_of_elements  # Create a list of size n filled with True values
current_index = 0                       # Set the current index to 0
step = 1                                 # Set the initial step to 1

# Step 3: Loop until step exceeds 500,000
while step <= 500000:
    # Check if the current position in is_true is True
    if is_true[current_index]:
        is_true[current_index] = False  # Set that position to False if it's True
    
    step += 1                            # Increment step by 1
    current_index = (current_index + step) % number_of_elements  # Update current index

# Step 4: Filter the list for remaining True values
remaining_true = [value for value in is_true if value]  # Create a new list with True values

# Step 5: Check outcome
if len(remaining_true) == 0:
    print("YES")                        # Output "YES" if length is 0
else:
    print("NO")                         # Output "NO" otherwise
