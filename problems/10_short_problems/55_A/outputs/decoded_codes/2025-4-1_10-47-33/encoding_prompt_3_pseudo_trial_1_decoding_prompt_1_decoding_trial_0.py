# Step 1: Read an integer input representing the size of the list
listSize = int(input())

# Step 2: Initialize a list of boolean values, all set to True
isActive = [True] * listSize

# Step 3: Initialize control variables
indexIncrement = 1
currentIndex = 0

# Step 4: Iterate through a range up to 500000
while currentIndex <= 500000:
    # Step 5: Check the boolean value at the current index
    if isActive[currentIndex]:
        # Mark the current index as inactive
        isActive[currentIndex] = False

    # Step 6: Update the index values
    indexIncrement += 1
    currentIndex = (currentIndex + indexIncrement) % listSize

# Step 7: Extract all True values from the isActive list
activeElements = [element for element in isActive if element]

# Step 8: Check if the activeElements list is empty
if len(activeElements) == 0:
    # If there are no active elements, print YES
    print('YES')
else:
    # If there are active elements, print NO
    print('NO')
