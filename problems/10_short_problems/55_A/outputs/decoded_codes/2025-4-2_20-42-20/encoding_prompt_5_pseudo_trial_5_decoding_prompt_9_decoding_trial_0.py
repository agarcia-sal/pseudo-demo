# Get Number of Elements
n = int(input())  # Read an integer value for the number of elements

# Initialize List
isActive = [True] * n  # Create a list of n elements, all set to True

# Set Initial Indices
currentIndex = 0  # Start pointing to the first element
step = 1  # Initial step value

# Process the List
while step <= 500000:
    if isActive[currentIndex]:  # Check if the current element is active
        isActive[currentIndex] = False  # Mark the current element as inactive
    
    step += 1  # Increment the step for the next iteration
    currentIndex = (currentIndex + step) % n  # Update the index with wrapping

# Check Remaining Active Elements
remainingActive = [item for item in isActive if item]  # Filter to find active elements

# Output Result
if len(remainingActive) == 0:  # Check if there are no remaining active elements
    print("YES")
else:
    print("NO")
