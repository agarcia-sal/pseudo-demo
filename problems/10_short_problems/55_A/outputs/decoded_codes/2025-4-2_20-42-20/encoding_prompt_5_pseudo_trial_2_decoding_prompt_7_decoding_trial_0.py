# Start Program

# Retrieve Input
n = int(input())  # Read the size of the list

# Initialize List
status = [True] * n  # Create a list called status with n elements, all set to true

# Initialize Variables
index = 0  # This will track the current position in the list
increment = 1  # This will determine how we progress through the list

# Perform Modifications
while increment <= 500000:  # Continue until increment exceeds 500000
    if status[index]:  # Check if the current element is true (active)
        status[index] = False  # Mark this element as inactive
    
    increment += 1  # Prepare for the next step
    index = (index + increment) % n  # Update index and wrap around if necessary

# Check Remaining Active Elements
active_elements = [value for value in status if value]  # Create a list of all true values from status

# Determine Output
if len(active_elements) == 0:  # Check if there are no active elements left
    print("YES")  # All elements are inactive
else:
    print("NO")  # There are still active elements

# End Program
