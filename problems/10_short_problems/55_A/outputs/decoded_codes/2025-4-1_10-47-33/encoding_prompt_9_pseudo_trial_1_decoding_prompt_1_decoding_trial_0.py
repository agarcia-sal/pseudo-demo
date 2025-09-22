# 1. Input the total number of positions
totalPositions = int(input())

# 2. Initialize a list to track marked positions
markedPositions = [True] * totalPositions  # All positions initially unmarked

# 3. Set initial index values
currentIndex = 0
step = 1

# 4. Mark positions in a loop
while step <= 500000:
    if markedPositions[currentIndex]:  # If the position is unmarked
        markedPositions[currentIndex] = False  # Mark the position
    step += 1  # Increment step
    currentIndex = (currentIndex + step) % totalPositions  # Update current index

# 5. Check for unmarked positions
unmarkedPositions = [pos for pos in markedPositions if pos]  # List of unmarked positions (True values)

# 6. Output results
if not unmarkedPositions:  # If there are no unmarked positions
    print("YES")
else:
    print("NO")
