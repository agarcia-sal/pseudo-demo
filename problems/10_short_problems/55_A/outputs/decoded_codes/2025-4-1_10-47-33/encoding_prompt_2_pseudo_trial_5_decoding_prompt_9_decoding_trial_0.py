# Start of the program
# Get an integer input representing the total number of elements
totalElements = int(input())

# Create a list called booleanList with all elements initially set to True
booleanList = [True] * totalElements

# Initialize variables
currentIndex = 0
increment = 1

# Start the loop
while increment <= 500000:
    # Check if the current position in booleanList is True
    if booleanList[currentIndex] is True:
        # Set that position in booleanList to False
        booleanList[currentIndex] = False
    
    # Increase the value of increment by 1
    increment += 1
    
    # Update currentIndex and wrap around using modulo
    currentIndex = (currentIndex + increment) % totalElements

# Create a new list containing all True elements from booleanList
remainingTrueValues = [value for value in booleanList if value]

# Check the length of remainingTrueValues
if len(remainingTrueValues) == 0:
    print("YES")  # Output "YES" if no True values remain
else:
    print("NO")   # Output "NO" if there are still True values
# End of the program
