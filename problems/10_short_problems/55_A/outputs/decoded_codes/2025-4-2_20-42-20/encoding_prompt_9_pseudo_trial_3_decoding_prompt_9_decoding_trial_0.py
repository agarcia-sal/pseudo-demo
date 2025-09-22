# Start the program

# Accept input for the size of the boolean array
size = int(input())

# Initialize the boolean array with all values set to True
status = [True] * size

# Set initial variables
index = 0
increment = 1

# Loop until increment exceeds 500,000
while increment <= 500000:
    # Check current status at the index
    if status[index]:
        # Set the status at the current index to False
        status[index] = False
    
    # Update increment and index
    increment += 1
    index = (index + increment) % size

# Filter active status to find all True values remaining in status
active_status = [s for s in status if s]

# Determine if any True elements exist in active_status
if len(active_status) == 0:
    print("YES")  # All elements are False
else:
    print("NO")   # There are still some True elements

# End the program
