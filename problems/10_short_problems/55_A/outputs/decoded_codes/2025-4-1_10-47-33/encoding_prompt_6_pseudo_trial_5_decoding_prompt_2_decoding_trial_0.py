# START

# Read the total number of elements
totalElements = int(input())

# Initialize a list to track status of each element, all set to True initially
statusList = [True] * totalElements

currentIndex = 0
iterationCounter = 1

# Loop until the iteration counter exceeds 500000
while iterationCounter <= 500000:
    # If the current position in the status list is True, change it to False
    if statusList[currentIndex] is True:
        statusList[currentIndex] = False

    # Increment the iteration counter
    iterationCounter += 1
    
    # Update the index in the status list using the current iteration
    currentIndex = (currentIndex + iterationCounter) % totalElements

# Create a list of all positions that are still True
remainingTrueStatus = [status for status in statusList if status]

# Check if there are no elements remaining that are True
if len(remainingTrueStatus) == 0:
    print('YES')  # Indicating all elements have been marked
else:
    print('NO')   # Indicating some elements are still marked true

# END
