# Step 1: Input the total number of positions
totalPositions = int(input())

# Step 2: Initialize a list to track marked positions
markedPositions = [True] * totalPositions

# Step 3: Set initial index values
currentIndex = 0
step = 1

# Step 4: Mark positions in a loop
while step <= 500000:
    if markedPositions[currentIndex]:  # Check if position is unmarked
        markedPositions[currentIndex] = False  # Mark the position

    step += 1  # Increment step
    currentIndex = (currentIndex + step) % totalPositions  # Update current index

# Step 5: Check for unmarked positions
unmarkedPositions = [pos for pos in markedPositions if pos]

# Step 6: Output results
if not unmarkedPositions:  # Check if there are any unmarked positions
    print("YES")
else:
    print("NO")
