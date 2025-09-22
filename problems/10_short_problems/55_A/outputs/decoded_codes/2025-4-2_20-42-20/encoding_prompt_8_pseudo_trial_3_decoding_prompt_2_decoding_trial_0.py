# Step 1: Initialize Input
n = int(input())

# Step 2: Create Boolean List
booleanList = [True] * n

# Step 3: Set Initial Positions
currentIndex = 0
increment = 1

# Step 4: Update Loop
limit = 500000
while increment <= limit:
    if booleanList[currentIndex]:
        booleanList[currentIndex] = False
    increment += 1
    currentIndex = (currentIndex + increment) % n  # Update currentIndex with wrap-around

# Step 5: Check Remaining True Values
remainingTrue = [b for b in booleanList if b]

# Step 6: Output Result
if len(remainingTrue) == 0:
    print('YES')
else:
    print('NO')
