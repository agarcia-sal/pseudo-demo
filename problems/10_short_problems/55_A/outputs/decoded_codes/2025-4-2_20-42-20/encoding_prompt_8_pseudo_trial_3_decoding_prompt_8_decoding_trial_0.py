# Initialize Input
n = int(input())

# Create Boolean List
booleanList = [True] * n

# Set Initial Positions
currentIndex = 0
increment = 1

# Update Loop
limit = 500000
while increment <= limit:
    if booleanList[currentIndex]:
        booleanList[currentIndex] = False
    increment += 1
    currentIndex = (currentIndex + increment) % n

# Check Remaining True Values
remainingTrue = [value for value in booleanList if value]

# Output Result
if len(remainingTrue) == 0:
    print('YES')
else:
    print('NO')
