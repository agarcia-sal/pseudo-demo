# Read an integer input representing the size of the list
n = int(input())

# Create a boolean list initialized to True with size n
isActive = [True] * n

# Initialize index variables for operation
currentIndex = 0
step = 1

# Loop until step exceeds 500,000
while step <= 500000:
    # If the current position in the list is marked True
    if isActive[currentIndex]:
        # Mark the current position as False
        isActive[currentIndex] = False

    # Increment step counter
    step += 1
    
    # Update currentIndex using modulo operation for wrapping
    currentIndex = (currentIndex + step) % n

# Filter the list to find all active positions (True values)
activePositions = [index for index, value in enumerate(isActive) if value]

# Check if there are no active positions remaining
if len(activePositions) == 0:
    print('YES')  # No active positions remain
else:
    print('NO')   # There are active positions remaining
