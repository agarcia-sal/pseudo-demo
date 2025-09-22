# Get input
n = int(input())  # Read the size of the boolean list from user input

# Initialize list
is_active = [True] * n  # Create a list of size n with all elements initialized to True

# Initialize counters
current_index = 0  # Index variable to track the current position
step_number = 1  # Counting variable to determine the step taken for index modification

# Iterate to modify list
while step_number <= 500000:
    if is_active[current_index]:  # Check if current position is True
        is_active[current_index] = False  # Set the current position to False

    step_number += 1  # Increase stepNumber by 1
    current_index = (current_index + step_number) % n  # Update the current index with wrapping

# Check remaining active elements
remaining_active = [value for value in is_active if value]  # List of remaining True elements

# Determine output
if len(remaining_active) == 0:
    print("YES")  # All elements are False
else:
    print("NO")  # At least one element remains True
