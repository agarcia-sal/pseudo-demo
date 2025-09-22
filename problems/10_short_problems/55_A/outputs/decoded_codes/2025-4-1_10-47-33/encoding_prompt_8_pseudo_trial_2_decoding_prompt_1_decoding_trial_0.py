# 1. Get Input
n = int(input())

# 2. Initialize List
isActive = [True] * n

# 3. Initialize Counters
currentIndex = 0
stepNumber = 1

# 4. Iterate to Modify List
while stepNumber <= 500000:
    if isActive[currentIndex]:
        isActive[currentIndex] = False  # Set the current position to False
    stepNumber += 1
    currentIndex = (currentIndex + stepNumber) % n  # Update index wrapping around

# 5. Check Remaining Active Elements
remainingActive = [x for x in isActive if x]

# 6. Determine Output
if len(remainingActive) == 0:
    print("YES")  # All elements have been changed to False
else:
    print("NO")   # At least one element remains True
