# Step 1: Receive Input
list_size = int(input())

# Step 2: Initialize Boolean List
boolean_list = [True] * list_size

# Step 3: Initialize Iteration Variables
current_index = 0
step = 1

# Step 4: Loop through iterations
while step <= 500000:
    # Check if the current position is True
    if boolean_list[current_index]:
        boolean_list[current_index] = False  # Set to False if True
    
    # Increment step and update current_index
    step += 1
    current_index = (current_index + step) % list_size  # Wrap around if necessary

# Step 5: Check Remaining True Values
remaining_true = [value for value in boolean_list if value]

# Step 6: Output Result
if len(remaining_true) == 0:
    print("YES")
else:
    print("NO")
