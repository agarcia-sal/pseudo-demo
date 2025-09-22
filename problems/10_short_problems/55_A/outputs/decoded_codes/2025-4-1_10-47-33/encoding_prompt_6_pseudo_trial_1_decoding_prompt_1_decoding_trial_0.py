# START

# Read the integer input which represents the size of the list
sizeOfList = int(input())

# Create a boolean list initialized to True with the specified size
booleanList = [True] * sizeOfList

# Initialize loop counters
counter = 1
currentIndex = 0

# Loop until counter exceeds 500,000
while counter <= 500000:
    # If the current index in the boolean list is True
    if booleanList[currentIndex] is True:
        # Mark the current index as False
        booleanList[currentIndex] = False

    # Increment the counter
    counter += 1

    # Update currentIndex based on the modulo of sizeOfList
    currentIndex = (currentIndex + counter) % sizeOfList

# Create a list of all True values from the boolean list
remainingTrueValues = [value for value in booleanList if value]

# Check if any True values remain
if len(remainingTrueValues) == 0:
    # If no True values left, print "YES"
    print("YES")
else:
    # If there are True values left, print "NO"
    print("NO")

# END
