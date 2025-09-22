# Input the size of the list
n = int(input())

# Initialize a list to track boolean values
isMarked = [True] * n

# Set initial variables for iteration
currentIndex = 0
stepCount = 1

# Start a loop to iterate while the step count is less than or equal to 500,000
while stepCount <= 500000:
    # Check if the current position in the isMarked list is True
    if isMarked[currentIndex]:
        isMarked[currentIndex] = False  # Mark it as False (processed)

    stepCount += 1  # Increment step count
    currentIndex = (currentIndex + stepCount) % n  # Update currentIndex

# Check how many elements remain unmarked
unmarkedElements = [marked for marked in isMarked if marked]

# Determine and output the result
if len(unmarkedElements) == 0:
    print("YES")  # All can be marked
else:
    print("NO")   # There remain unmarked elements
