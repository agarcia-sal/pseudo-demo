# Step 1: Get Input Value
n = int(input())

# Step 2: Initialize List
booleanList = [True] * n

# Step 3: Initialize Counters
step = 1
index = 0

# Step 4: Process Values
while step <= 500000:
    if booleanList[index]:
        booleanList[index] = False
    step += 1
    index = (index + step) % n

# Step 5: Check for Remaining True Values
remainingTrue = [value for value in booleanList if value]

# Step 6: Output Result
if not remainingTrue:
    print('YES')
else:
    print('NO')
