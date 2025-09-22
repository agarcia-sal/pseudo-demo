# Start of the Program

# Input Handling
numberOfElements = int(input())

# Initialization
statusList = [True] * numberOfElements
currentIndex = 0
stepIncrement = 1

# Looping Process
while stepIncrement <= 500000:
    if statusList[currentIndex]:
        statusList[currentIndex] = False
    stepIncrement += 1
    currentIndex = (currentIndex + stepIncrement) % numberOfElements

# Filtering Results
trueValues = [value for value in statusList if value]

# Output Handling
if len(trueValues) == 0:
    print("YES")
else:
    print("NO")

# End of the Program
