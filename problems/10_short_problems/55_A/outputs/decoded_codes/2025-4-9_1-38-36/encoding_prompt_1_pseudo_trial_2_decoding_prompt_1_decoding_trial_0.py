# Step 1: Input Size
n = int(input())

# Step 2: Initialize List
boolList = [True] * n
j = 0  # index to track the current position
i = 1  # index to control the number of iterations

# Step 3: Sequential Operations
while i <= 500000:
    if boolList[j] == True:
        boolList[j] = False  # mark the position as processed
    i += 1  # increment the iteration count
    j = (j + i) % n  # update j with the modulus operation

# Step 4: Check Remaining True Values
remainingTrue = [value for value in boolList if value == True]

# Step 5: Output Result
if not remainingTrue:  # check if remainingTrue is empty
    print('YES')
else:
    print('NO')
