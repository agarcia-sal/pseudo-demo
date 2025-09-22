# Step 1: Receive input for the number of elements
number_of_elements = int(input())

# Step 2: Create a list called flags with all entries set to True
flags = [True] * number_of_elements

# Step 3: Initialize index and counter
index = 0
counter = 1

# Step 4: Start a loop that runs while counter is less than or equal to 500000
while counter <= 500000:
    # Check if the current entry in flags is True
    if flags[index]:
        # Set the entry to False
        flags[index] = False
    # Increment the counter for the next iteration
    counter += 1
    # Update the index
    index = (index + counter) % number_of_elements

# Step 5: Create a new list active_flags that includes only True entries
active_flags = [flag for flag in flags if flag]

# Step 6: Check the length of active_flags and output the result
if len(active_flags) == 0:
    print("YES")  # All entries in flags are False
else:
    print("NO")   # Some entries in flags remain True
