# Get Input
n = int(input())

# Initialize List
isActive = [True] * n

# Initialize Counters
currentIndex = 0
stepNumber = 1

# Iterate to Modify List
while stepNumber <= 500000:
    if isActive[currentIndex]:
        isActive[currentIndex] = False
    stepNumber += 1
    currentIndex = (currentIndex + stepNumber) % n

# Check Remaining Active Elements
remainingActive = [active for active in isActive if active]

# Determine Output
if len(remainingActive) == 0:
    print("YES")
else:
    print("NO")
