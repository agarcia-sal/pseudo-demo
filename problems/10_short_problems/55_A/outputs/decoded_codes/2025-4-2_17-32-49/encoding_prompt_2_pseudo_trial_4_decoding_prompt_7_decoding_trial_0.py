# Start of the program

# Input: Read an integer value n (number of elements)
n = int(input())

# Initialize: Create a list isAvailable with n elements, all set to True
isAvailable = [True] * n  # List to track availability of positions
position = 0               # Initialize position to track current index
step = 1                   # Initialize step to increment

# Loop until step exceeds 500,000
while step <= 500000:
    # Check if current position is available
    if isAvailable[position]: 
        # Mark this position as unavailable
        isAvailable[position] = False  
    
    # Increment step
    step += 1
    
    # Update position using remainder of division
    position = (position + step) % n  

# Check for available positions
availablePositions = [i for i in isAvailable if i]  # Gather all True values

# Output Result
if len(availablePositions) == 0:  # If no positions are available
    print("YES")  # All positions marked unavailable
else:
    print("NO")   # Some positions are still available

# End of the program
