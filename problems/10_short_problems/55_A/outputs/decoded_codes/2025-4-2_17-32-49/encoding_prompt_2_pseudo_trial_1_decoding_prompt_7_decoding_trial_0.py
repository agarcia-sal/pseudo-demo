# Step 1: Receive an input value that represents the number of elements
numberOfElements = int(input())

# Step 2: Create a list called booleanList and initialize all elements to True
booleanList = [True] * numberOfElements

# Step 3: Initialize the index to 0
index = 0

# Step 4: Set the step variable to 1
step = 1

# Step 5: Begin the process that continues as long as step is less than or equal to 500,000
while step <= 500000:
    # Check if the current position in booleanList at index is True
    if booleanList[index]:
        # If it is True, change the current position in booleanList to False
        booleanList[index] = False
    
    # Increment the step variable by 1
    step += 1
    
    # Update the index by adding step and taking modulo numberOfElements
    index = (index + step) % numberOfElements

# Step 6: Collect all elements from booleanList that are still True into a new list called trueElements
trueElements = [i for i in range(numberOfElements) if booleanList[i]]

# Step 7: Check the length of trueElements and output the appropriate message
if len(trueElements) == 0:
    print("YES")  # output if there are no True elements
else:
    print("NO")   # output if there are True elements
