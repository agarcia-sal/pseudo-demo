# Step 1: Get Number of Elements
n = int(input())

# Step 2: Initialize List
isActive = [True] * n

# Step 3: Set Initial Indices
currentIndex = 0
step = 1

# Step 4: Process the List
while step <= 500000:
    if isActive[currentIndex]:  # Check if current element is True
        isActive[currentIndex] = False  # Mark it as False (deactivate it)
    
    step += 1  # Increment step for the next iteration
    currentIndex = (currentIndex + step) % n  # Update currentIndex with wrap around

# Step 5: Check Remaining Active Elements
remainingActive = [x for x in isActive if x]  # Filter the isActive list for True values

# Step 6: Output Result
if len(remainingActive) == 0:
    print("YES")  # No active elements left
else:
    print("NO")  # Active elements still remain
