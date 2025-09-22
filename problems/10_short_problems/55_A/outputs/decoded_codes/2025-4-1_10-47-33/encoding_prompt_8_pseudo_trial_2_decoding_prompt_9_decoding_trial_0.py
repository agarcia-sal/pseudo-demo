# Step 1: Get Input
n = int(input())  # Read an integer value from the user

# Step 2: Initialize List
isActive = [True] * n  # Create a list with n elements all set to True

# Step 3: Initialize Counters
currentIndex = 0  # Starting index
stepNumber = 1  # Starting counting number

# Step 4: Iterate to Modify List
while stepNumber <= 500000:
    if isActive[currentIndex]:  # Check if the current position is True
        isActive[currentIndex] = False  # Set it to False (remove/mark inactive)

    stepNumber += 1  # Increase the counting variable
    currentIndex = (currentIndex + stepNumber) % n  # Update the index with wrapping

# Step 5: Check Remaining Active Elements
remainingActive = [value for value in isActive if value]  # Create a list of active (True) values

# Step 6: Determine Output
if len(remainingActive) == 0:  # Check if there are no remaining True values
    print("YES")  # All elements have been changed to False
else:
    print("NO")  # At least one element remains True
