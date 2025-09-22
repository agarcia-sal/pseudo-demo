# Initialize Variables
numberOfPositions = int(input())
markedPositions = [True] * numberOfPositions  # Create a list initialized to True
currentIndex = 0  # Counter for the current index
stepCount = 1  # Step counter starts at 1

# Perform Marking Process
while stepCount <= 500000:  # Loop until stepCount exceeds 500,000
    if markedPositions[currentIndex]:  # Check if the current position is marked
        markedPositions[currentIndex] = False  # Mark this position as False
    
    stepCount += 1  # Increment the step count
    currentIndex = (currentIndex + stepCount) % numberOfPositions  # Update the current index

# Check for Unmarked Positions
unmarkedPositions = [pos for pos in markedPositions if pos]  # Create a list of unmarked positions
if not unmarkedPositions:  # Check if the list of unmarked positions is empty
    print("YES")  # All positions marked
else:
    print("NO")  # Unmarked positions remain
