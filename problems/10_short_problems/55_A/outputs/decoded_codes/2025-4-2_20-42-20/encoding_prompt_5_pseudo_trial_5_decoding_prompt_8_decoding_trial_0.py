# Get Number of Elements
n = int(input())

# Initialize List
isActive = [True] * n

# Set Initial Indices
currentIndex = 0
step = 1

# Process the List
while step <= 500000:
    if isActive[currentIndex]:
        isActive[currentIndex] = False
    step += 1
    currentIndex = (currentIndex + step) % n

# Check Remaining Active Elements
remainingActive = [x for x in isActive if x]

# Output Result
if len(remainingActive) == 0:
    print("YES")
else:
    print("NO")
