# Step 1: Start (implied by starting the program in Python)

# Step 2: Input
n = int(input())

# Step 3: Initialize
isActive = [True] * n  # Create a list of size 'n' with all elements set to True

# Step 4: Set Variables
nextIndex = 0          # Set variable 'nextIndex' to 0
currentStep = 1        # Set variable 'currentStep' to 1

# Step 5: Loop
while currentStep <= 500000:
    if isActive[nextIndex]:  # If 'isActive[nextIndex]' is True
        isActive[nextIndex] = False  # Mark this index as inactive
    currentStep += 1  # Increment 'currentStep' by 1
    nextIndex = (nextIndex + currentStep) % n  # Update 'nextIndex' with wrapping

# Step 6: Filter Active Elements
activeElements = [i for i in range(n) if isActive[i]]  # Create a list of active indices

# Step 7: Output
if len(activeElements) == 0:  # If there are no active elements left
    print('YES')              # Print 'YES'
else:
    print('NO')               # Otherwise, print 'NO'

# Step 8: End (implied by end of the program)
