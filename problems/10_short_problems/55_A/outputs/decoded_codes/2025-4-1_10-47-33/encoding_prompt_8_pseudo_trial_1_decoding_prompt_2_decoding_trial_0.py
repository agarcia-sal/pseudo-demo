# Start Program

# Get Input
n = int(input())  # Read an integer value from the user

# Initialize List
IsMarked = [True] * n  # Create a list of size n, where all elements are True (unmarked)

# Initialize Counters
currentIndex = 0  # Variable to track which index is being operated on
increment = 1  # Step size for marking the list

# Marking Process
while increment <= 500000:
    if IsMarked[currentIndex]:  # Check if current index is still marked as True
        IsMarked[currentIndex] = False  # Mark this item as processed (set to False)
    
    increment += 1  # Increment the marking step
    currentIndex = (currentIndex + increment) % n  # Update currentIndex with wrap-around

# Check for Unmarked Items
UnmarkedItems = [item for item in IsMarked if item]  # Create a list of items that are still True

# Output Result
if len(UnmarkedItems) == 0:  # Check if there are any unmarked items
    print('YES')  # All items are marked
else:
    print('NO')  # There are unmarked items

# End Program
