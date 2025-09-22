# Step 1: Receive Input
n = int(input())

# Step 2: Initialize List
isMarked = [True] * n

# Step 3: Set Initial Values
currentPosition = 0
step = 1

# Step 4: Process Marking
while step <= 500000:
    if isMarked[currentPosition]:  # Check if the current position is still True
        isMarked[currentPosition] = False  # Mark it as False
    step += 1  # Increment step
    currentPosition = (currentPosition + step) % n  # Move to next position wrapping around using modulo n

# Step 5: Check Marking Results
unmarkedPositions = [pos for pos in isMarked if pos]  # Create list of unmarked positions

# Step 6: Output Result
if len(unmarkedPositions) == 0:
    print('YES')  # All positions were marked
else:
    print('NO')   # There are still unmarked positions
