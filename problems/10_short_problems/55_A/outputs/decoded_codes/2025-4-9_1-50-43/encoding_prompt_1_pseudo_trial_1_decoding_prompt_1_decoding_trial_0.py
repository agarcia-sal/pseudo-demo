# Step 1: Take an integer input for the size of the array (n)
n = int(input())

# Step 2: Initialize an array 'markedPositions' of size n with all values set to True
markedPositions = [True] * n

# Step 3: Set a variable 'currentPosition' to 0
currentPosition = 0

# Step 4: Set a variable 'stepSize' to 1
stepSize = 1

# Step 5: While 'stepSize' is less than or equal to 500000
while stepSize <= 500000:
    # Step 5a: Check if 'markedPositions[currentPosition]' is True
    if markedPositions[currentPosition]:
        # Step 5ai: Mark the current position as False
        markedPositions[currentPosition] = False
    
    # Step 5b: Increase 'stepSize' by 1
    stepSize += 1
    
    # Step 5c: Update 'currentPosition' to the next position using the formula
    currentPosition = (currentPosition + stepSize) % n

# Step 6: Create a list 'unmarkedPositions' containing the positions from 'markedPositions' where the value is still True
unmarkedPositions = [i for i in range(n) if markedPositions[i]]

# Step 7: If the length of 'unmarkedPositions' is 0
if len(unmarkedPositions) == 0:
    # Step 7a: Output 'YES'
    print('YES')
# Step 8: Else
else:
    # Step 8a: Output 'NO'
    print('NO')
