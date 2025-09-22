# Start Program

# Accept Input
size = int(input())  # Set size to the integer value received from user input

# Initialize Array
status = [True] * size  # Create a boolean array status of length size, filled with True

# Set Initial Variables
index = 0
increment = 1

# Loop until a condition is met
while increment <= 500000:  # While increment is less than or equal to 500,000
    # Check Current Status
    if status[index]:  # If status[index] is True
        status[index] = False  # Set status[index] to False
    
    # Update Values
    increment += 1  # Increment increment by 1
    index = (index + increment) % size  # Update index

# Filter Active Status
active_status = [s for s in status if s]  # Create a list of all elements from status that are still True

# Determine If Any True Elements Exist
if len(active_status) == 0:  # If the length of active_status is 0
    print("YES")  # Print "YES"
else:
    print("NO")  # Otherwise, print "NO"

# End Program
