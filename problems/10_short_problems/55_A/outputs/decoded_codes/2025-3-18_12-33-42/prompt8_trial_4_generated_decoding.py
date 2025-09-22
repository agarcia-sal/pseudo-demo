# Start Program
n = int(input())

# Initialize List
isMarked = [True] * n

# Set Initial Variables
currentIndex = 0
step = 1

# Mark Elements
while step <= 500000:
    if isMarked[currentIndex]:
        isMarked[currentIndex] = False
    step += 1
    currentIndex = (currentIndex + step) % n

# Check Remaining True Elements
remainingTrue = [mark for mark in isMarked if mark]

# Output Result
if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")
