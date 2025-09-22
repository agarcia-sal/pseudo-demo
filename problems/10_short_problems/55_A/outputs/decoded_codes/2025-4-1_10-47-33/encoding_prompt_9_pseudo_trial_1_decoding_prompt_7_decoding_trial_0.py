# Step 1: Input the total number of positions
totalPositions = int(input())

# Step 2: Initialize a list to track marked positions
# All positions are initially unmarked (True)
markedPositions = [True] * totalPositions

# Step 3: Set initial index values
currentIndex = 0  # This will track the current position in the list
step = 1  # This will define the increment in indices as we mark positions

# Step 4: Mark positions in a loop
while step <= 500000:
    # Check if the current position is unmarked
    if markedPositions[currentIndex]:
        # Mark the current position as False
        markedPositions[currentIndex] = False
    
    # Increment the step
    step += 1
    # Update currentIndex using the formula given
    currentIndex = (currentIndex + step) % totalPositions

# Step 5: Check for unmarked positions
# Create a list of unmarked positions that are still True
unmarkedPositions = [pos for pos in markedPositions if pos]

# Step 6: Output results
if not unmarkedPositions:  # If the list is empty, all positions are marked
    print("YES")
else:  # Otherwise, some positions are still unmarked
    print("NO")
