# Initialize the Program
n = int(input())  # Read an integer value n from user input.

# Create a boolean list
isActive = [True] * n  # Create a list with n elements, all initialized to True.

# Set initial positions
index = 0  # Set a variable index to 0
step = 1   # Set a variable step to 1

# Iterate through steps
while step <= 500000:  # Repeat while step is less than or equal to 500,000
    if isActive[index]:  # Check if isActive[index] is True
        isActive[index] = False  # Change isActive[index] to False
        
    step += 1  # Increment step by 1
    index = (index + step) % n  # Update index and wrap around using modulo n

# Check remaining active positions
activePositions = [pos for pos in isActive if pos]  # Create a list of active positions

# Determine the output
if len(activePositions) == 0:  # Check if there are no True values left
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"
