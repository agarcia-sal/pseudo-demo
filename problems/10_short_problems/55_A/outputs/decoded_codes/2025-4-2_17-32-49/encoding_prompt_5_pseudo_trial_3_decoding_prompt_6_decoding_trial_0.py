# Start Program

# Receive Input
n = int(input())  # Read a number n which represents the size of the list

# Initialize Boolean List
boolean_list = [True] * n  # Create a list with all elements initialized to True

# Set Up Iteration Variables
current_index = 0  # This will track the current position in boolean_list
step = 1  # This will dictate how far to move through the list during marking

# Mark Elements Process
while step <= 500000:  # Continue until step exceeds 500000
    # Check Current Position
    if boolean_list[current_index]:  # If the current position is True (unmarked)
        boolean_list[current_index] = False  # Mark this position as False (marked)

    # Increment Step Value
    step += 1  # Increase step by 1

    # Calculate Next Position
    current_index = (current_index + step) % n  # Update currentIndex using modulo n for wrapping

# Extract Remaining Unmarked Elements
remaining_true = [value for value in boolean_list if value]  # List of unmarked positions

# Check Results
if len(remaining_true) == 0:  # If there are no unmarked positions
    print("YES")  # All positions were marked
else:
    print("NO")  # At least one position remained unmarked

# End Program
