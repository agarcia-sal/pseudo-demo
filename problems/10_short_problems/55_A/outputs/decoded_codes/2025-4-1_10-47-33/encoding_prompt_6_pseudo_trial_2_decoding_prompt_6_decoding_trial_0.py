# Start of the program

# Step 1: Receive input value for n
number_of_elements = int(input())  # Convert input to an integer

# Step 2: Initialize a boolean list to track elements
is_active = [True] * number_of_elements  # List of 'True' of size number_of_elements

# Step 3: Initialize index variables for the loop
index = 0  # Start index
increment = 1  # Initial increment value

# Step 4: Loop through numbers while the increment value is less than or equal to 500,000
while increment <= 500000:  
    # Step 5: Check if the current index in the boolean list is active
    if is_active[index]:  # If the current index is still active
        # Step 6: Mark the current index as inactive
        is_active[index] = False  # Set the index to inactive (False)

    # Step 7: Move to the next increment
    increment += 1  # Increment the increment variable

    # Step 8: Update the index based on the current increment while ensuring it wraps around
    index = (index + increment) % number_of_elements  # Wrap-around using modulus

# Step 9: Create a list of active elements from the boolean list
active_elements = [i for i, active in enumerate(is_active) if active]  # List of indices where is_active is True

# Step 10: Check if there are active elements left
if len(active_elements) == 0:  # If there are no active elements
    # Step 11: If no active elements, output 'YES'
    print('YES')  # Print 'YES' if all were marked inactive
else:
    # Step 12: Otherwise, output 'NO'
    print('NO')  # Print 'NO' if there are still active indices

# End of the program
