# Start of the program

# Step 1: Read the integer input for the size of the array
numberOfElements = int(input())

# Step 2: Initialize a boolean array with 'True' values for each index
isActive = [True] * numberOfElements

# Step 3: Initialize variables for current index and increment value
currentIndex = 0
incrementValue = 1

# Step 4: Loop until the incrementValue exceeds 500,000
while incrementValue <= 500000:
    
    # Step 5: Check if the current index in the boolean array is still marked as active
    if isActive[currentIndex]:
        # Step 6: Set the current index to inactive
        isActive[currentIndex] = False
    
    # Step 7: Move to the next increment
    incrementValue += 1
    
    # Step 8: Update the current index using modulo operation to wrap around the boolean array
    currentIndex = (currentIndex + incrementValue) % numberOfElements

# Step 9: Create a list of active indices based on the boolean array
activeElements = [index for index, value in enumerate(isActive) if value]

# Step 10: Check if there are any active elements remaining
if len(activeElements) == 0:
    print('YES')  # No active elements found
else:
    print('NO')   # Active elements still present

# End of the program
