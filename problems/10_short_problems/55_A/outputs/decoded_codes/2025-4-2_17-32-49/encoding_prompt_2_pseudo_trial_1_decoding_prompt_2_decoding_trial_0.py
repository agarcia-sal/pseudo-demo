# Step 1: Receive the input
numberOfElements = int(input())

# Step 2: Create a list called booleanList initialized to True
booleanList = [True] * numberOfElements

# Step 3: Initialize index to 0
index = 0

# Step 4: Initialize step to 1
step = 1

# Step 5: Loop while step is less than or equal to 500,000
while step <= 500000:
    # Check if current position in booleanList is True
    if booleanList[index]:
        # Change the current position in booleanList to False
        booleanList[index] = False
    
    # Increment the step variable by 1
    step += 1
    
    # Update index using the current value of step
    index = (index + step) % numberOfElements

# Step 6: Collect all elements from booleanList that are still True
trueElements = [i for i in booleanList if i]

# Step 7: Check the length of trueElements
if len(trueElements) == 0:
    # Step 7.1: Output "YES" if trueElements is empty
    print("YES")
else:
    # Step 7.2: Output "NO" otherwise
    print("NO")
