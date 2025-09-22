# Step 1: Read an integer number 'n' from user input
n = int(input())

# Step 2: Create a list called 'status' with 'n' elements, all set to True
status = [True] * n

# Step 3: Initialize the variables
current_step = 1  # Current step counter
index = 0  # Starting index

# Step 4: Loop while 'current_step' is less than or equal to 500000
while current_step <= 500000:
    # Step 5: Check the status of the current index
    if status[index]:
        # Set the status at the current index to False
        status[index] = False
    
    # Step 6: Increment current step
    current_step += 1
    
    # Step 7: Update the index using MOD operator
    index = (index + current_step) % n

# Step 8: Filter for active status elements
active_elements = [s for s in status if s]

# Step 9: Check the result based on length of active elements
if len(active_elements) == 0:
    print("YES")  # Print "YES" if there are no active elements
else:
    print("NO")   # Print "NO" if there are active elements
