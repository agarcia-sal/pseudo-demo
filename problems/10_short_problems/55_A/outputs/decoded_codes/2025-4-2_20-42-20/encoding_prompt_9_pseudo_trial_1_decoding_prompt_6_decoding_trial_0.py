# Read the total number of elements from the user
total_elements = int(input())

# Initialize the markings list with all elements set to True
markings = [True] * total_elements

# Set initial index and step variables
current_index = 0
current_step = 1

# Start the marking process
while current_step <= 500000:
    if markings[current_index]:  # If the current item is still marked as True
        markings[current_index] = False  # Mark it as False (processed)
    
    current_step += 1  # Increment the step
    current_index = (current_index + current_step) % total_elements  # Update index, wrapped around using modulo

# Check remaining marked items
remaining_true = [mark for mark in markings if mark]  # Create a list of items still marked as True

# Output result based on whether any items are still marked True
if len(remaining_true) == 0:
    print("YES")  # All items have been marked
else:
    print("NO")  # At least one item is still unmarked
