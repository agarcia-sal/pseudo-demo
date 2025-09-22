# Step 1: Initialize Input
numberOfElements = int(input())  # Read the number of elements from the user

# Step 2: Create a Boolean List
isActive = [True] * numberOfElements  # List to track which positions are still active

# Step 3: Set Initial Indices
currentIndex = 0  # Starting index
stepSize = 1      # Initial step size for elimination

# Step 4: Start Elimination Process
while stepSize <= 500000:
    if isActive[currentIndex]:  # Check if current position is active
        isActive[currentIndex] = False  # Mark this position as eliminated
    stepSize += 1  # Increment the step size
    currentIndex = (currentIndex + stepSize) % numberOfElements  # Update index with wrap-around

# Step 5: Check Remaining Active Entries
remainingActive = [active for active in isActive if active]  # Create a list of remaining active positions

# Step 6: Determine and Print Final Result
if len(remainingActive) == 0:  # If no positions are active
    print("YES")  # All positions have been eliminated
else:
    print("NO")  # There are still active positions
