# Start of the Program

# Input Handling: Read the number of elements from the user
numberOfElements = int(input())

# Initialization: Create a status list with all True values
statusList = [True] * numberOfElements

# Initialize index and stepIncrement
currentIndex = 0
stepIncrement = 1

# Looping Process: Repeat while stepIncrement is less than or equal to 500,000
while stepIncrement <= 500000:
    # Check the value at currentIndex in the statusList
    if statusList[currentIndex]:
        # If the value is True, set it to False
        statusList[currentIndex] = False
    
    # Increment the stepIncrement by 1
    stepIncrement += 1
    
    # Update currentIndex and wrap around if necessary
    currentIndex = (currentIndex + stepIncrement) % numberOfElements

# Filtering Results: Create a list of remaining True values
trueValues = [value for value in statusList if value]

# Output Handling: Check the length of trueValues
if len(trueValues) == 0:
    print("YES")
else:
    print("NO")

# End of the Program
