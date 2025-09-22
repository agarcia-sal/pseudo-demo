# Start of the program

# Retrieve input
n = int(input())  # Read an integer value for the size of the list

# Initialize list with all elements set to true
status = [True] * n

# Initialize variables
index = 0
increment = 1

# Perform modifications
while increment <= 500000:
    if status[index]:  # Check if the current element is active
        status[index] = False  # Mark the current element as inactive
    increment += 1  # Prepare for the next step
    index = (index + increment) % n  # Update index, wrapping around if necessary

# Check remaining active elements
active_elements = [element for element in status if element]  # Collect all true values

# Determine output
if len(active_elements) == 0:  # If there are no active elements
    print("YES")  # All elements are inactive
else:
    print("NO")  # There are still active elements

# End of the program
