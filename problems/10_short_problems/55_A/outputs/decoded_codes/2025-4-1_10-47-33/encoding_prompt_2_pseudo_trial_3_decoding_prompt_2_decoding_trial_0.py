# Start of the Program

# Input Handling
numberOfElements = int(input())

# Initialization
statusList = [True] * numberOfElements  # Create a list of size numberOfElements initialized to True
currentIndex = 0
stepIncrement = 1

# Looping Process
while stepIncrement <= 500000:  # Repeat as long as stepIncrement is less than or equal to 500,000
    if statusList[currentIndex]:  # Check the value at currentIndex
        statusList[currentIndex] = False  # Set that value to False
    stepIncrement += 1  # Increment stepIncrement by 1
    currentIndex = (currentIndex + stepIncrement) % numberOfElements  # Update currentIndex and wrap around

# Filtering Results
trueValues = [value for value in statusList if value]  # Create a new list with elements that are still True

# Output Handling
if len(trueValues) == 0:  # Check the length of trueValues
    print("YES")  # If length is 0, print "YES"
else:
    print("NO")  # Else, print "NO"

# End of the Program
