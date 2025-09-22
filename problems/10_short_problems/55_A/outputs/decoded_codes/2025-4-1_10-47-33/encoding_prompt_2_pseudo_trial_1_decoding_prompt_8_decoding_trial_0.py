# Step 1: Initialize Input
numberOfElements = int(input())

# Step 2: Create a Boolean List
isActive = [True] * numberOfElements

# Step 3: Set Initial Indices
currentIndex = 0
stepSize = 1

# Step 4: Start Elimination Process
while stepSize <= 500000:
    if isActive[currentIndex]:
        isActive[currentIndex] = False  # Eliminate the current position

    stepSize += 1
    currentIndex = (currentIndex + stepSize) % numberOfElements  # Update current index

# Step 5: Check Remaining Active Entries
remainingActive = [active for active in isActive if active]

# Step 6: Determine and Print Final Result
if len(remainingActive) == 0:
    print("YES")
else:
    print("NO")
