# Start of the program

# Step 2: Accept Input
size = int(input())  # Get the size from user input as an integer

# Step 3: Initialize Array
status = [True] * size  # Create a boolean array of length `size` initialized with True

# Step 4: Set Initial Variables
index = 0  # Start index at 0
increment = 1  # Initial increment value

# Step 5: Loop until a condition is met
while increment <= 500000:
    # Step 1: Check Current Status
    if status[index]:  # If the current status at index is True
        status[index] = False  # Set it to False
    
    # Step 2: Update Values
    increment += 1  # Increment increment by 1
    index = (index + increment) % size  # Update index using modulo size

# Step 6: Filter Active Status
active_status = [s for s in status if s]  # Create a list of True elements

# Step 7: Determine If Any True Elements Exist
if len(active_status) == 0:  # Check if the active_status list is empty
    print("YES")  # Print YES if no True elements exist
else:
    print("NO")  # Print NO if there are True elements

# End of the program
