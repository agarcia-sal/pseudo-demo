# Read the total number of elements from the user
n = int(input())

# Initialize the marking list with all elements set to True
markings = [True] * n

# Set initial variables
index = 0  # Tracks the current position
step = 1   # Indicates the current counting step

# Start the marking process
while step <= 500000:
    if markings[index]:  # Check if the current item is marked True
        markings[index] = False  # Mark it as processed (False)
    
    step += 1  # Increment the step count
    index = (index + step) % n  # Update the index, wrapping around using modulo n

# Check for the remaining marked items
remainingTrue = [item for item in markings if item]  # List of items still marked True

# Output the result
if len(remainingTrue) == 0:  # Check if no item is marked True
    print("YES")
else:
    print("NO")
