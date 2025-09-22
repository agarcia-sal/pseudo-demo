# Step 1: Receive input for number of elements
numberOfElements = int(input())

# Step 2: Create a list of boolean values initialized to True
booleanList = [True] * numberOfElements

# Step 3: Initialize the index
index = 0

# Step 4: Initialize the step
step = 1

# Step 5: Loop while step is less than or equal to 500,000
while step <= 500000:
    # Check if the current position in booleanList is True
    if booleanList[index]:
        # If it is True, set it to False
        booleanList[index] = False
    
    # Increment the step
    step += 1
    
    # Update the index with wrapping around using modulo
    index = (index + step) % numberOfElements

# Step 6: Collect all elements from booleanList that are still True
trueElements = [elem for elem in booleanList if elem]

# Step 7: Check the length of trueElements
if len(trueElements) == 0:
    print("YES")
else:
    print("NO")
