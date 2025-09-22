# Start of the Program

# Input Handling: Read an integer value from the user
numberOfElements = int(input())

# Initialization: Create a list of size numberOfElements initialized to True
statusList = [True] * numberOfElements
currentIndex = 0
stepIncrement = 1

# Looping Process: Repeat until stepIncrement exceeds 500,000
while stepIncrement <= 500000:
    # Check the value at currentIndex in the statusList
    if statusList[currentIndex]:
        # If the value is True, set that value to False
        statusList[currentIndex] = False
    
    # Increment stepIncrement by 1
    stepIncrement += 1
    
    # Update currentIndex with wrap around
    currentIndex = (currentIndex + stepIncrement) % numberOfElements

# Filtering Results: Create a list of still True values
trueValues = [value for value in statusList if value]

# Output Handling: Check the length of trueValues
if len(trueValues) == 0:
    print("YES")
else:
    print("NO")

# End of the Program
