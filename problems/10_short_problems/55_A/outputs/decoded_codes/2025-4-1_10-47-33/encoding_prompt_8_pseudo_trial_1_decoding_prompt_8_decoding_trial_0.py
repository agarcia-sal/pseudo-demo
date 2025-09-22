# Start Program

# Get Input
n = int(input())

# Initialize List
IsMarked = [True] * n

# Initialize Counters
currentIndex = 0
increment = 1

# Marking Process
while increment <= 500000:
    if IsMarked[currentIndex]:
        IsMarked[currentIndex] = False  # Mark this item as processed
    increment += 1
    currentIndex = (currentIndex + increment) % n  # Wrap around if needed

# Check for Unmarked Items
UnmarkedItems = [item for item in IsMarked if item]  # Items that are still True

# Output Result
if len(UnmarkedItems) == 0:  # All items are marked
    print('YES')
else:
    print('NO')

# End Program
