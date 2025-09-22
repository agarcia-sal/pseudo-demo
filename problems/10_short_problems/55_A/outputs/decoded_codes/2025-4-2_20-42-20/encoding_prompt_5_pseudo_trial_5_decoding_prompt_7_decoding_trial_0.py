# Step 1: Get Number of Elements
n = int(input())  # Read an integer value for the number of elements in the list

# Step 2: Initialize List
isActive = [True] * n  # Create a list of size n filled with True values

# Step 3: Set Initial Indices
currentIndex = 0  # Start from the first element
step = 1  # Initial step value

# Step 4: Process the List
while step <= 500000:  # Repeat until step exceeds 500,000
    if isActive[currentIndex]:  # Check if the current element is True (active)
        isActive[currentIndex] = False  # Deactivate the element by setting it to False
    
    # Update for the next iteration
    step += 1  # Increment the step
    currentIndex = (currentIndex + step) % n  # Update currentIndex with wrapping around

# Step 5: Check Remaining Active Elements
remainingActive = [value for value in isActive if value]  # Filter for True values in isActive

# Step 6: Output Result
if len(remainingActive) == 0:  # Check if there are no active elements left
    print("YES")  # Output "YES" if no active elements remain
else:
    print("NO")  # Output "NO" otherwise
