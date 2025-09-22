# Start of the program

# Step 1: Read the number of elements from input
numberOfElements = int(input())

# Step 2: Create a list to track active elements, initialized to True
isActive = [True] * numberOfElements

# Step 3: Initialize the current index and the current step
index = 0
step = 1

# Step 4: Loop until the step exceeds 500000
while step <= 500000:
    # Step 4a: Check if the current index is active
    if isActive[index]:
        # Mark the index as inactive
        isActive[index] = False
    
    # Step 4b: Increment the step
    step += 1
    
    # Step 4c: Update the current index
    index = (index + step) % numberOfElements

# Step 5: Create a list of active elements
activeElements = [active for active in isActive if active]

# Step 6: Check if there are any active elements left
if len(activeElements) == 0:
    # Step 6a: Print 'YES' if no active elements are remaining
    print('YES')
else:
    # Step 6b: Print 'NO' if there are still active elements
    print('NO')

# End of the program
