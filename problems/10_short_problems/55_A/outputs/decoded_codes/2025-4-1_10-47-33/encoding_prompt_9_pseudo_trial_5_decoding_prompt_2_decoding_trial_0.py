# Initialize Variables
numberOfPositions = int(input())
markedPositions = [True] * numberOfPositions
currentIndex = 0
stepCount = 1

# Perform Marking Process
while stepCount <= 500000:
    if markedPositions[currentIndex]:
        markedPositions[currentIndex] = False  # Mark this position as False
    stepCount += 1
    currentIndex = (currentIndex + stepCount) % numberOfPositions  # Update index with wrap-around

# Check for Unmarked Positions
unmarkedPositions = [pos for pos in markedPositions if pos]  # List of True values

if not unmarkedPositions:  # If no True values remain
    print("YES")
else:
    print("NO")
