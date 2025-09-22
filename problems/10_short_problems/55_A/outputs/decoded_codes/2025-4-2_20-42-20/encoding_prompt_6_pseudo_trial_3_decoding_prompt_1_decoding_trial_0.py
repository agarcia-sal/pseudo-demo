# Step 1: Read an integer input which represents the size of a list.
listSize = int(input())

# Step 2: Create a boolean list initialized to True for all indices up to listSize.
booleanList = [True] * listSize

# Step 3: Initialize variables for iteration.
currentIndex = 0
increment = 1

# Step 4: Loop until increment reaches 500,000.
while increment <= 500000:
    
    # Step 5: Check if the current index in the boolean list is True.
    if booleanList[currentIndex]:
        
        # Step 6: Set the current index in the boolean list to False.
        booleanList[currentIndex] = False

    # Step 7: Increment the counter for the next iteration.
    increment += 1
    
    # Step 8: Calculate the next index by adding the increment and wrapping around the list using modulus.
    currentIndex = (currentIndex + increment) % listSize

# Step 9: Create a new list containing all the True values from the boolean list.
remainingTrueValues = [value for value in booleanList if value]

# Step 10: Check if there are any remaining True values.
if len(remainingTrueValues) == 0:
    
    # Step 11: If no True values remain, print 'YES'.
    print('YES')
else:
    
    # Step 12: If there are still True values, print 'NO'.
    print('NO')
