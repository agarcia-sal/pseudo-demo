# Step 1: Get the size of the list from user input
numberOfPositions = int(input())

# Step 2: Create a list called 'marks' to track the status of each position
marks = [True] * numberOfPositions

# Step 3: Initialize counters
currentIndex = 0  # This will track our current position in the list
incrementValue = 1  # This value will be used to determine the step size for marking

# Step 4: Start a loop that continues until incrementValue exceeds 500,000
while incrementValue <= 500000:

    # Step 5: Check if the current position is still marked as True
    if marks[currentIndex]:
        # Step 6: Mark the current position as False
        marks[currentIndex] = False

    # Step 7: Prepare for the next iteration
    incrementValue += 1  # Increase the step size
    currentIndex = (currentIndex + incrementValue) % numberOfPositions  # Update the current index

# Step 8: Filter the marks list to find any position still marked as True
remainingTruePositions = [mark for mark in marks if mark]

# Step 9: Check the result of the filtering
if len(remainingTruePositions) == 0:
    # If there are no True positions left, print "YES"
    print('YES')
else:
    # If there are still True positions left, print "NO"
    print('NO')
