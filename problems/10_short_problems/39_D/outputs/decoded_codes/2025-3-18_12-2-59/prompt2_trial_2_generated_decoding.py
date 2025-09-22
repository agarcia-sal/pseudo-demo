# Begin the main process

# Receive input from the user
firstInput = input()
secondInput = input()

# Split the input lines into individual elements
firstList = firstInput.split()
secondList = secondInput.split()

# Initialize a counter for differences
differenceCount = 0 

# Compare each corresponding element in the two lists
for index in range(3):
    valueA = int(firstList[index])
    valueB = int(secondList[index])

    # Check if the values are different
    if valueA != valueB:
        differenceCount += 1 

# Determine the output based on the number of differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End the main process
