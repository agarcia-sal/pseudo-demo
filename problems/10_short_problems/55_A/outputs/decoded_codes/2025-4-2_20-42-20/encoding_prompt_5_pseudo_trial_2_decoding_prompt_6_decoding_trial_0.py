# Start of the program

# Retrieve input for the size of the list
n = int(input())

# Initialize the list with `n` elements set to True
status = [True] * n

# Initialize the index and increment variables
index = 0
increment = 1

# Perform modifications based on the defined conditions
while increment <= 500000:
    if status[index]:  # Check if the current element is active
        status[index] = False  # Mark the current element as inactive
    increment += 1  # Increase increment for next step
    index = (index + increment) % n  # Update index while wrapping around

# Create a new list to capture all active (True) values
active_elements = [i for i in status if i]

# Determine the output based on the length of active elements
if len(active_elements) == 0:
    print("YES")  # All elements are inactive
else:
    print("NO")  # There are still active elements

# End of the program
