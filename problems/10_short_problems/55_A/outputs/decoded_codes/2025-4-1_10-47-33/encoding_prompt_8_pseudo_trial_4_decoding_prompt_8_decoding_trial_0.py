# Step 1: Read Input
totalNumbers = int(input())

# Step 2: Initialize List
statusList = [True] * totalNumbers  

# Step 3: Set Initial Indices
currentIndex = 0
step = 1

# Step 4: Loop Until Limit Reached
while step <= 500000:
    if statusList[currentIndex]:
        statusList[currentIndex] = False
    step += 1
    currentIndex = (currentIndex + step) % totalNumbers  

# Step 5: Check Remaining True Values
remainingTrueValues = [value for value in statusList if value]

# Step 6: Output Result
if len(remainingTrueValues) == 0:
    print("YES")
else:
    print("NO")
