# Start by receiving an input value that represents the number of elements
numberOfElements = int(input())

# Create a list called booleanList with a size equal to numberOfElements, initialized to True
booleanList = [True] * numberOfElements

# Set a variable index to 0, which keeps track of the current position in the booleanList
index = 0

# Set another variable step to 1, which controls the increment of the index
step = 1

# Continue the process as long as step is less than or equal to 500,000
while step <= 500000:
    # Check if the current position in booleanList (at index) is True
    if booleanList[index]:
        # If it is True, change the current position (at index) in booleanList to False
        booleanList[index] = False

    # Increment the step variable by 1
    step += 1

    # Update the index by adding the current value of step and wrapping around using modulo
    index = (index + step) % numberOfElements

# Collect all elements from booleanList that are still True into a new list called trueElements
trueElements = [i for i in booleanList if i]

# Check the length of trueElements
if len(trueElements) == 0:
    # If trueElements is empty, output the message "YES"
    print("YES")
else:
    # Otherwise, output the message "NO"
    print("NO")
