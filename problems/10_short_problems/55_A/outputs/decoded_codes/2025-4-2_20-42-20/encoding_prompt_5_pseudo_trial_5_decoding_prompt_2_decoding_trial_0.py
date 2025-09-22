# Step 1: Get Number of Elements
n = int(input())

# Step 2: Initialize List
isActive = [True] * n

# Step 3: Set Initial Indices
currentIndex = 0
step = 1

# Step 4: Process the List
while step <= 500000:
    # Check if the current element is True
    if isActive[currentIndex]:
        # Mark this element as False
        isActive[currentIndex] = False

    # Increment the step for the next iteration
    step += 1

    # Update the currentIndex using modulo n
    currentIndex = (currentIndex + step) % n

# Step 5: Check Remaining Active Elements
remainingActive = [x for x in isActive if x]

# Step 6: Output Result
if len(remainingActive) == 0:
    print("YES")
else:
    print("NO")
