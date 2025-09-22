# Step 1: Start

# Step 2: Receive Input
list_size = int(input())

# Step 3: Initialize Boolean List
boolean_list = [True] * list_size

# Step 4: Initialize Iteration Variables
current_index = 0
step = 1

# Step 5: Loop through iterations
while step <= 500000:
    if boolean_list[current_index]:  # Check if current position is True
        boolean_list[current_index] = False  # Set that position to False
    step += 1  # Increment step by 1
    current_index = (current_index + step) % list_size  # Update current_index

# Step 6: Check Remaining True Values
remaining_true = [value for value in boolean_list if value]

# Step 7: Output Result
if len(remaining_true) == 0:
    print("YES")
else:
    print("NO")

# Step 8: End
