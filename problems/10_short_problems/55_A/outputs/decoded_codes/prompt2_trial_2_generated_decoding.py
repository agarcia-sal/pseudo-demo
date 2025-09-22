# Step 1: Read input
size = int(input())

# Step 2: Initialize the isAvailable list
isAvailable = [True] * size

# Step 3: Initialize counters
currentIndex = 0
step = 1

# Step 4: Loop to mark items as unavailable
while step <= 500000:
    if isAvailable[currentIndex]:  # Check if the current item is available
        isAvailable[currentIndex] = False  # Mark it as unavailable
    step += 1  # Increment step counter
    currentIndex = (currentIndex + step) % size  # Update currentIndex with wrap-around

# Step 5: Create a list of available items
availableItems = [item for item in isAvailable if item]  # Collect all items that are still True

# Step 6: Check if there are any available items
if len(availableItems) == 0:
    print('YES')  # All items are marked as unavailable
else:
    print('NO')   # There are still available items
