# Read an integer value n from user input
n = int(input())

# Initialize a list isPresent of size n, with all values set to True
isPresent = [True] * n
index = 0  # Variable to track the current position
step = 1   # Variable to dictate how many positions to move forward

# Processing loop that continues while step is less than or equal to 500,000
while step <= 500000:
    # Check if the current position is available
    if isPresent[index]:
        # Mark the position as unavailable
        isPresent[index] = False
        
    # Increment step by 1
    step += 1
    
    # Update index to the next position
    index = (index + step) % n  # Ensure the index stays within bounds

# Create a new list availablePositions containing all the True values from isPresent
availablePositions = [pos for pos in isPresent if pos]

# Check the length of availablePositions and print the corresponding result
if len(availablePositions) == 0:
    print("YES")  # All positions are marked as not available
else:
    print("NO")   # There are still available positions
