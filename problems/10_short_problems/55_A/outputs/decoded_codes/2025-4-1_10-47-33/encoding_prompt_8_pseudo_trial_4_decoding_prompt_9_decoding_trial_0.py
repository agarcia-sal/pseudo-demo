# Read input to get the total number of entries
totalNumbers = int(input())

# Initialize the status list with all values set to True
statusList = [True] * totalNumbers

# Set initial indices
currentIndex = 0
step = 1

# Loop until the step limit of 500000 is reached
while step <= 500000:
    if statusList[currentIndex]:  # If the current index in statusList is True
        statusList[currentIndex] = False  # Mark it as False
    step += 1  # Increase step by 1
    currentIndex = (currentIndex + step) % totalNumbers  # Circular update of currentIndex

# Check for remaining True values in statusList
remainingTrueValues = [value for value in statusList if value]

# Output result based on the number of remaining True values
if len(remainingTrueValues) == 0:
    print("YES")  # No True values remaining
else:
    print("NO")  # At least one True value remains
