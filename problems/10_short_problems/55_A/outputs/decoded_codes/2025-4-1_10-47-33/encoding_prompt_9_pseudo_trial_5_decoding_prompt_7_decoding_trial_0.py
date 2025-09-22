# Initialize Variables
numberOfPositions = int(input())  # Get an integer value from user input
markedPositions = [True] * numberOfPositions  # Create a list of True values
currentIndex = 0  # Initialize the current index
stepCount = 1  # Initialize step count

# Perform Marking Process
while stepCount <= 500000:  # Loop until stepCount exceeds 500,000
    if markedPositions[currentIndex]:  # Check if the current position is marked
        markedPositions[currentIndex] = False  # Mark the position as False (unmarked)
    
    stepCount += 1  # Increment the step count
    # Update currentIndex using the formula provided
    currentIndex = (currentIndex + stepCount) % numberOfPositions  # Wrap around the list

# Check for Unmarked Positions
unmarkedPositions = [pos for pos in markedPositions if pos]  # List all True values (unmarked)

# Output based on whether there are unmarked positions
if not unmarkedPositions:  # If the list of unmarkedPositions is empty
    print("YES")  # All positions are marked
else:
    print("NO")  # There are still unmarked positions
