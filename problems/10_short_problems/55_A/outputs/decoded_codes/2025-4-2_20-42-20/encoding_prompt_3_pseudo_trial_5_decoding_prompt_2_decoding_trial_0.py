# Step 1: Read an integer input representing the size of the list.
numberOfElements = int(input())

# Step 2: Initialize a list with boolean values set to True.
booleanList = [True] * numberOfElements

# Step 3: Initialize variables for counting and indexing.
index = 0
increment = 1

# Step 4: Iterate while increment is less than or equal to 500,000.
while increment <= 500000:
    # Step 5: Check if the current index in booleanList is True.
    if booleanList[index]:
        # Step 6: If True, set the current index in booleanList to False.
        booleanList[index] = False
    
    # Step 7: Increment the value of increment.
    increment += 1

    # Step 8: Update index using the formula to wrap around the list.
    index = (index + increment) % numberOfElements

# Step 9: Create a new list of elements from booleanList that are still True.
activeElementsList = [value for value in booleanList if value]

# Step 10: Check if there are any True elements in the activeElementsList.
if len(activeElementsList) == 0:
    # If no True elements remain, output 'YES'.
    print('YES')
else:
    # Otherwise, output 'NO'.
    print('NO')
