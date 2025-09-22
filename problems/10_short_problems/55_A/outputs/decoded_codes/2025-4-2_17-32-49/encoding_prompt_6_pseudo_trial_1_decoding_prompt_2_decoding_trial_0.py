# Step 1: Input an integer value 'n'
n = int(input())

# Step 2: Initialize a list 'isActive' of size 'n' with all elements set to True
isActive = [True] * n

# Step 3: Set Variables
nextIndex = 0
currentStep = 1

# Step 4: Loop while 'currentStep' is less than or equal to 500,000
while currentStep <= 500000:
    # Step 4a: Check if 'isActive[nextIndex]' is True
    if isActive[nextIndex]:
        # Mark this index as inactive
        isActive[nextIndex] = False

    # Increment 'currentStep' by 1
    currentStep += 1

    # Update 'nextIndex' to ensure it wraps around within bounds of the list
    nextIndex = (nextIndex + currentStep) % n

# Step 5: Filter active elements
activeElements = [index for index, active in enumerate(isActive) if active]

# Step 6: Output results
if len(activeElements) == 0:
    print('YES')
else:
    print('NO')
