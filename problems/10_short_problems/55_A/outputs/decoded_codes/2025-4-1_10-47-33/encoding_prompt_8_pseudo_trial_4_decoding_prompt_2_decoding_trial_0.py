# 1. Read Input
totalNumbers = int(input())

# 2. Initialize List
statusList = [True] * totalNumbers

# 3. Set Initial Indices
currentIndex = 0
step = 1

# 4. Loop Until Limit Reached
while step <= 500000:
    if statusList[currentIndex] == True:
        # a. Change statusList[currentIndex] to False
        statusList[currentIndex] = False
        
    # b. Increase step by 1
    step += 1
    
    # c. Update currentIndex
    currentIndex = (currentIndex + step) % totalNumbers

# 5. Check Remaining True Values
remainingTrueValues = [x for x in statusList if x]

# 6. Output Result
if len(remainingTrueValues) == 0:
    print("YES")
else:
    print("NO")
