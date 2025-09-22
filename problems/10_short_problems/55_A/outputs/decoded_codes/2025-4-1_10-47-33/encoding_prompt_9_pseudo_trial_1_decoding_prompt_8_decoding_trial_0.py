# Input the total number of positions:
totalPositions = int(input())

# Initialize a list to track marked positions:
markedPositions = [True] * totalPositions

# Set initial index values:
currentIndex = 0
step = 1

# Mark positions in a loop:
while step <= 500000:
    if markedPositions[currentIndex]:  # If the position is unmarked
        markedPositions[currentIndex] = False  # Mark it
    
    step += 1  # Increment step
    currentIndex = (currentIndex + step) % totalPositions  # Update currentIndex

# Check for unmarked positions:
unmarkedPositions = [pos for pos in markedPositions if pos]

# Output results:
if not unmarkedPositions:
    print("YES")
else:
    print("NO")
