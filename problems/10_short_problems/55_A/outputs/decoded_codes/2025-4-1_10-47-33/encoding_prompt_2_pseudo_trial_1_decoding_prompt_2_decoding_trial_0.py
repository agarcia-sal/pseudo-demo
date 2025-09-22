# Initialize Input
numberOfElements = int(input())

# Create a Boolean List
isActive = [True] * numberOfElements

# Set Initial Indices
currentIndex = 0
stepSize = 1

# Start Elimination Process
while stepSize <= 500000:
    if isActive[currentIndex]:
        isActive[currentIndex] = False  # Eliminate the current position
    stepSize += 1
    currentIndex = (currentIndex + stepSize) % numberOfElements  # Update index

# Check Remaining Active Entries
remainingActive = [active for active in isActive if active]  # List remaining active positions

# Determine and Print Final Result
if len(remainingActive) == 0:  # No active positions remain
    print("YES")
else:  # There are still some active positions
    print("NO")
