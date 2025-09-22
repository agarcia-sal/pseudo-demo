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
        isActive[currentIndex] = False  # Marking position as inactive (False)
    
    stepNumber += 1
    currentIndex = (currentIndex + stepNumber) % n  # Wrap around using modulo

# Check Remaining Active Elements
remainingActive = [active for active in isActive if active]

# Determine Output
if len(remainingActive) == 0:
    print("YES")  # All elements are False
else:
    print("NO")   # At least one element is True
