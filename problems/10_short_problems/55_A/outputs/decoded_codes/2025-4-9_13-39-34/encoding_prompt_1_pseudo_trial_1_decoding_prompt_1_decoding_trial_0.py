# Start: Begin the program.

# Read Input
input_number = input()  # Prompt the user for a number
size = int(input_number)  # Convert input to an integer and store it in 'size'

# Initialize Boolean List
boolean_list = [True] * size  # Create a list with 'size' elements, all set to True

# Initialize Index Variables
current_index = 0  # Track the position in the list
step_count = 1  # Determine how many steps to skip

# Loop
while step_count <= 500000:  # While step_count is less than or equal to 500,000
    # Check Boolean Value
    if boolean_list[current_index]:  # If the current boolean value is True
        boolean_list[current_index] = False  # Mark it as False
    
    step_count += 1  # Increment step_count by 1
    current_index = (current_index + step_count) % size  # Update current_index based on step_count

# Filter Remaining True Values
remaining_true = [value for value in boolean_list if value]  # Create a list of remaining True values

# Check Remaining Elements
if len(remaining_true) == 0:  # If the length of remaining_true is 0
    print("YES")  # All were marked False
else:
    print("NO")  # Some remain True

# End: Finish the program.
