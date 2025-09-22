# Read a positive integer from the user
totalCount = int(input())

# Initialize a list of boolean values set to True
booleanList = [True] * totalCount

# Initialize index variables
step = 1
currentIndex = 0

# Perform operations
while step <= 500000:
    if booleanList[currentIndex]:  # Check if the current boolean is True
        booleanList[currentIndex] = False  # Set it to False
    step += 1
    currentIndex = (currentIndex + step) % totalCount  # Update the current index

# Create a list containing all True values
trueValues = [value for value in booleanList if value]

# Determine the output
if len(trueValues) == 0:
    print("YES")
else:
    print("NO")
