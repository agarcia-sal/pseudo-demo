# 1. Initialize Input:
numberOfElements = int(input())

# 2. Create a Boolean List:
isActive = [True] * numberOfElements

# 3. Set Initial Indices:
currentIndex = 0
stepSize = 1

# 4. Start Elimination Process:
while stepSize <= 500000:
    if isActive[currentIndex]:
        isActive[currentIndex] = False  # Mark as eliminated

    stepSize += 1
    currentIndex = (currentIndex + stepSize) % numberOfElements  # Update index

# 5. Check Remaining Active Entries:
remainingActive = [active for active in isActive if active]  # List of active entries

# 6. Determine and Print Final Result:
if len(remainingActive) == 0:
    print("YES")  # All positions eliminated
else:
    print("NO")   # Some positions are still active
