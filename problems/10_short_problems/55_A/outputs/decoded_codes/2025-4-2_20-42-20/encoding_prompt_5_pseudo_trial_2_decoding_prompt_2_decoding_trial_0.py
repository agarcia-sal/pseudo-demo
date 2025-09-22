# Start Program

# Retrieve Input
n = int(input())  # Read an integer value n that represents the size of a list.

# Initialize List
status = [True] * n  # Create a list called status with n elements, all set to true.

# Initialize Variables
index = 0  # Set a variable index to 0
increment = 1  # Set a variable increment to 1

# Perform Modifications
while increment <= 500000:  # While the value of increment is less than or equal to 500000
    if status[index]:  # If status[index] is true (the current element is active)
        status[index] = False  # Mark the current element as inactive
    increment += 1  # Increase increment by 1
    index = (index + increment) % n  # Update index using the formula

# Check Remaining Active Elements
active_elements = [value for value in status if value]  # Create a new list of all true values in status

# Determine Output
if len(active_elements) == 0:  # If the length of active_elements is 0
    print("YES")  # Print "YES"
else:
    print("NO")  # Else, print "NO"

# End Program
