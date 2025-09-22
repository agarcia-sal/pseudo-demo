# Start of the program

# Step 1: Accept the size of the boolean list from user input
n = int(input())  # Read size of the boolean list as an integer

# Step 2: Create a boolean list of size n with all values initially set to True
boolean_list = [True] * n  # Initialize the list with True values

# Step 3: Initialize index variables
current_index = 0  # Start index
increment = 1  # Initial increment value

# Step 4: Loop to update the boolean list
while increment <= 500000:
    # Step 4a: If the value at the current index is True
    if boolean_list[current_index]:
        # Step 4b: Set the value at the current index to False
        boolean_list[current_index] = False
    
    # Step 4c: Update the increment and move to the next index
    increment += 1  # Increase increment by 1
    current_index = (current_index + increment) % n  # Move to the next index, wrap around if exceeds n

# Step 5: Check for any True values left in the boolean list
remaining_true_values = [value for value in boolean_list if value]  # List of all True values

# Step 6: Determine the result based on the presence of True values
if len(remaining_true_values) == 0:
    print("YES")  # No True values remain
else:
    print("NO")   # There are still True values present

# End of the program
