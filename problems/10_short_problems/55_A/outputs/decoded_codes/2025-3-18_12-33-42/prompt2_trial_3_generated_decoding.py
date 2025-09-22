# Step 1: Input
listSize = int(input())

# Step 2: Initialize
booleanList = [True] * listSize  # Create a list of True values of size listSize

# Step 3: Set Initial Values
index = 0
currentValue = 1

# Step 4: Loop Until Limit
while currentValue <= 500000:
    if booleanList[index]:  # Check if booleanList[index] is True
        booleanList[index] = False  # Change it to False

    currentValue += 1  # Increase currentValue by 1
    index = (index + currentValue) % listSize  # Update index within bounds using modulo

# Step 5: Extract True Values
trueValues = [value for value in booleanList if value]  # List of elements still True

# Step 6: Check Result
if len(trueValues) == 0:  # Check if there are no True values
    print('YES')
else:
    print('NO')
