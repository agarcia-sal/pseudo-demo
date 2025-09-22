# Initialize the Program by reading an integer value n from user input
n = int(input())

# Create a boolean list isActive with n elements, all initialized to True
isActive = [True] * n

# Set initial positions
index = 0  # This will track the current position in the list
step = 1   # This will determine how many steps to move after each iteration

# Iterate through steps while step is less than or equal to 500,000
while step <= 500000:
    # Check if the current position in isActive at index is True
    if isActive[index]:
        # If it is True, change that position in isActive to False
        isActive[index] = False
    
    # Increment step by 1
    step += 1
    
    # Update the index to be the current index plus step, wrapping around using modulo n
    index = (index + step) % n

# Check remaining active positions
activePositions = [active for active in isActive if active]

# Determine the output
if len(activePositions) == 0:
    # If the length of activePositions is 0, print "YES"
    print("YES")  # All positions have been deactivated
else:
    # Otherwise, print "NO"
    print("NO")   # There are still active positions
