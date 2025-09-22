# Step 1: Receive input value for the number of elements
numberOfElements = int(input())

# Step 2: Create and initialize the boolean list
booleanList = [True] * numberOfElements

# Step 3: Initialize variables
index = 0
step = 1

# Step 5: Process with steps until 500,000
while step <= 500000:
    # Check the current position in the boolean list
    if booleanList[index]:
        # Change the current position to False
        booleanList[index] = False
    
    # Increment the step variable
    step += 1
    
    # Update the index by adding step and wrapping around
    index = (index + step) % numberOfElements

# Step 6: Collect all True elements in a new list
trueElements = [i for i in booleanList if i]

# Step 7: Check the length of trueElements and output the result
if len(trueElements) == 0:
    print("YES")
else:
    print("NO")


def process_boolean_list(numberOfElements):
    booleanList = [True] * numberOfElements
    currentIndex = 0
    step = 1
    
    while step <= 500000:
        if booleanList[currentIndex]:
            booleanList[currentIndex] = False
        step += 1
        currentIndex = (currentIndex + step) % numberOfElements

    trueElements = [i for i in booleanList if i]

    if len(trueElements) == 0:
        return "YES"
    else:
        return "NO"

# Input and output handling
numberOfElements = int(input())
result = process_boolean_list(numberOfElements)
print(result)
