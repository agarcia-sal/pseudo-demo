# Step 1: Initialize Input
n = int(input())

# Step 2: Create Boolean Array
isAlive = [True] * n

# Step 3: Initialize Counters
currentStep = 1
currentIndex = 0

# Step 4: Loop Until Limit
while currentStep <= 500000:
    if isAlive[currentIndex]:
        isAlive[currentIndex] = False  # Mark this position as "dead"
    
    currentStep += 1
    currentIndex = (currentIndex + currentStep) % n  # Wrap around if it exceeds n

# Step 5: Collect Remaining Alive Positions
remainingAlive = [alive for alive in isAlive if alive]

# Step 6: Check for Remaining Alive Positions
if len(remainingAlive) == 0:
    print("YES")  # All positions are dead
else:
    print("NO")   # At least one position is alive
