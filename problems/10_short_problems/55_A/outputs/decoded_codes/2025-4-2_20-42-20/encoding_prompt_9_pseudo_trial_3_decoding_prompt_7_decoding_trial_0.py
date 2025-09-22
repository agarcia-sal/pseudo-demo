# Start Program

# Accept Input
size = int(input())  # Read the size of the boolean array from user input

# Initialize Array
status = [True] * size  # Create a boolean array of length 'size' and fill with True

# Set Initial Variables
index = 0  # Starting index
increment = 1  # Starting increment value

# Loop until a condition is met
while increment <= 500000:  # Continue looping until increment exceeds 500,000
    # Check Current Status
    if status[index]:  # If the current status at index is True
        status[index] = False  # Set the status at this index to False
    
    # Update Values
    increment += 1  # Increment the increment value
    index = (index + increment) % size  # Update index using modulo to wrap around

# Filter Active Status
active_status = [s for s in status if s]  # Create a list of all elements in 'status' that are still True

# Determine If Any True Elements Exist
if len(active_status) == 0:  # If there are no True elements left
    print("YES")  # Print "YES"
else:
    print("NO")  # Otherwise, print "NO"

# End Program
