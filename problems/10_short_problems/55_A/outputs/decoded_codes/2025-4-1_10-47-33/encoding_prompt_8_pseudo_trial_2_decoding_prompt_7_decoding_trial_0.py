# Step 1: Get Input
n = int(input())  # Read the size of the boolean list

# Step 2: Initialize List
isActive = [True] * n  # Create a list of size n with all elements set to True

# Step 3: Initialize Counters
currentIndex = 0  # Set the initial index to 0
stepNumber = 1  # Initialize a counting variable

# Step 4: Iterate to Modify List
while stepNumber <= 500000:
    if isActive[currentIndex]:  # Check if the current position is True
        isActive[currentIndex] = False  # Mark it as False
    stepNumber += 1  # Increment step number
    currentIndex = (currentIndex + stepNumber) % n  # Calculate new index with wrap around

# Step 5: Check Remaining Active Elements
remainingActive = [value for value in isActive if value]  # List of elements that are still True

# Step 6: Determine Output
if len(remainingActive) == 0:  # Check if there are no True values left
    print("YES")  # Print YES if all elements have been changed to False
else:
    print("NO")  # Print NO if at least one element remains True
