# Initialize the Program
n = int(input())  # Read an integer value n from user input

# Create a boolean list
isActive = [True] * n  # Create a list named isActive with n elements initialized to True

# Set initial positions
index = 0  # Initialize index to track the current position
step = 1   # Initialize step to determine how many steps to move after each iteration

# Iterate through steps
while step <= 500000:  # Repeat while step is less than or equal to 500,000
    if isActive[index]:  # Check if the current position in isActive at index is True
        isActive[index] = False  # Change that position in isActive to False
    step += 1  # Increment step by 1
    index = (index + step) % n  # Update index with wrapping around using modulo n

# Check remaining active positions
activePositions = [i for i in isActive if i]  # Create a new list including all elements from isActive that are still True

# Determine the output
if len(activePositions) == 0:  # If length of activePositions is 0
    print("YES")  # Indicating that all positions have been deactivated
else:
    print("NO")  # Indicating that there are still active positions
