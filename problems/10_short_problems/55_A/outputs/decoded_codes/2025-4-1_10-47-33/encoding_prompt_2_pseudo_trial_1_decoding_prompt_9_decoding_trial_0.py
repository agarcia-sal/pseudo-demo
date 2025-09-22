# Step 1: Read the number of elements from the user
numberOfElements = int(input())

# Step 2: Create a list to track active elements
isActive = [True] * numberOfElements  # Initialize all entries to True

# Step 3: Initialize current index and step size
currentIndex = 0
stepSize = 1

# Step 4: Start the elimination process
while stepSize <= 500000:
    if isActive[currentIndex]:  # Check if the current index is active
        isActive[currentIndex] = False  # Eliminate the element at the current index
    stepSize += 1  # Increment the step size
    currentIndex = (currentIndex + stepSize) % numberOfElements  # Update index

# Step 5: Check remaining active entries
remainingActive = [active for active in isActive if active]  # Filter out inactive elements

# Step 6: Determine and print final result
if len(remainingActive) == 0:
    print("YES")  # All positions eliminated
else:
    print("NO")   # Some positions are still active
