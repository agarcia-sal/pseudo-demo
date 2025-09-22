# Step 1: Initialize Variables
numberOfPositions = int(input())
markedPositions = [True] * numberOfPositions
currentIndex = 0
stepCount = 1

# Step 2: Perform Marking Process
while stepCount <= 500000:
    if markedPositions[currentIndex]:
        markedPositions[currentIndex] = False  # Mark current position as False
    stepCount += 1
    currentIndex = (currentIndex + stepCount) % numberOfPositions  # Update index

# Step 3: Check for Unmarked Positions
unmarkedPositions = [position for position in markedPositions if position]
if not unmarkedPositions:  # If there are no True values left
    print("YES")
else:
    print("NO")
