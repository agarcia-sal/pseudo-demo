# BEGIN
# Input: Read an integer value for the total count
totalCount = int(input())

# Initialize a list with 'totalCount' elements, all initially set to True
statusList = [True] * totalCount

# Initialize two counters
outerCounter = 1
indexCounter = 0

# Loop while the outer counter is less than or equal to 500,000
while outerCounter <= 500000:
    # If the current position in statusList is TRUE
    if statusList[indexCounter]:
        # Set the current position to FALSE
        statusList[indexCounter] = False

    # Increment the outer counter
    outerCounter += 1
    
    # Update the indexCounter using modulo operation to wrap around
    indexCounter = (indexCounter + outerCounter) % totalCount

# Filter the statusList to find all elements that are still TRUE
remainingTrue = [status for status in statusList if status]

# Check if there are no TRUE elements remaining
if len(remainingTrue) == 0:
    print('YES')
else:
    print('NO')
# END
