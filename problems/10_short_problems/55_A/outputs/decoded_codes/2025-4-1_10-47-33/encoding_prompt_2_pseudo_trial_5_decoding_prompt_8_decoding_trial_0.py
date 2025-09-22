# Begin the program
totalElements = int(input())
booleanList = [True] * totalElements  # Create a list with all elements set to true
currentIndex = 0
increment = 1

# Start the loop
while increment <= 500000:
    if booleanList[currentIndex]:  # Check if the current position is true
        booleanList[currentIndex] = False  # Set it to false
    increment += 1  # Increase increment by 1
    currentIndex = (currentIndex + increment) % totalElements  # Update currentIndex

# Create a list of remaining true values
remainingTrueValues = [value for value in booleanList if value]

# Check the length of remainingTrueValues
if len(remainingTrueValues) == 0:
    print("YES")
else:
    print("NO")
# End the program
