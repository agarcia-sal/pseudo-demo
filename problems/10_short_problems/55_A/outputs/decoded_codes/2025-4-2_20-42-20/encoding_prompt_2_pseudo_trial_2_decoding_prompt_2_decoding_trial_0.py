# Step 1: Start by receiving the integer input
number_of_elements = int(input())

# Step 2: Create a list of flags initialized to True
flags = [True] * number_of_elements

# Step 3: Initialize index and counter
index = 0
counter = 1

# Step 4: Loop until counter exceeds 500,000
while counter <= 500000:
    # Check the condition for the current entry in flags
    if flags[index]:
        # Set the current flag to False
        flags[index] = False
    
    # Increment counter by 1
    counter += 1
    # Update index with wrapping
    index = (index + counter) % number_of_elements

# Step 5: Create the active_flags list with remaining True values
active_flags = [flag for flag in flags if flag]

# Step 6: Check the length of active_flags and output accordingly
if len(active_flags) == 0:
    print("YES")
else:
    print("NO")
