# 1. Initialize Variables:
numberOfPositions = int(input())  # Get an integer value from user input.
markedPositions = [True] * numberOfPositions  # Create a list with `numberOfPositions` elements, all set to True.
currentIndex = 0  # Initialize currentIndex to 0
stepCount = 1  # Initialize stepCount to 1

# 2. Perform Marking Process:
while stepCount <= 500000:  # Loop until stepCount is greater than 500,000
    if markedPositions[currentIndex]:  # Check if the current position is True
        markedPositions[currentIndex] = False  # Mark this position as False
    stepCount += 1  # Increment the stepCount
    currentIndex = (currentIndex + stepCount) % numberOfPositions  # Update currentIndex

# 3. Check for Unmarked Positions:
unmarkedPositions = [position for position in markedPositions if position]  # Create a list of unmarked positions
if not unmarkedPositions:  # If unmarkedPositions is empty
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"
