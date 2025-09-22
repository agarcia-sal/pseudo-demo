# Step 1: Start (implicitly started by defining the function)

# Step 2: Input
totalElements = int(input())

# Step 3: Initialize
booleanList = [True] * totalElements

# Step 4: Set
currentIndex = 0
incrementalStep = 1

# Step 5: Loop
while incrementalStep <= 500000:
    # Check
    if booleanList[currentIndex]:
        # Update
        booleanList[currentIndex] = False
    
    # Increment
    incrementalStep += 1
    
    # Calculate
    currentIndex = (currentIndex + incrementalStep) % totalElements

# Step 6: Filter
trueElements = [element for element in booleanList if element]

# Step 7: Decision
if len(trueElements) == 0:
    # Output
    print('YES')
else:
    # Output
    print('NO')

# Step 8: End (implicitly ended as the script finishes execution)
