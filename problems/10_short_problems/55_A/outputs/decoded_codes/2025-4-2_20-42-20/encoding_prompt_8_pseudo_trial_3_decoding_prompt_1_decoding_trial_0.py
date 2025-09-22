# 1. Initialize Input
n = int(input())

# 2. Create Boolean List
booleanList = [True] * n

# 3. Set Initial Positions
currentIndex = 0
increment = 1

# 4. Update Loop
limit = 500000
while increment <= limit:
    if booleanList[currentIndex]:
        booleanList[currentIndex] = False
    increment += 1
    currentIndex = (currentIndex + increment) % n

# 5. Check Remaining True Values
remainingTrue = [value for value in booleanList if value]

# 6. Output Result
if len(remainingTrue) == 0:
    print('YES')
else:
    print('NO')
