# Begin the main process

# Prompt the user to input the first set of values
firstInput = input()
# Prompt the user to input the second set of values
secondInput = input()

# Split the first input string into a list of values
firstValues = firstInput.split()
# Split the second input string into a list of values
secondValues = secondInput.split()

# Initialize a counter variable called differenceCount
differenceCount = 0

# Loop through each index from 0 to 2 (inclusive)
for index in range(3):
    # Convert the value at the current index in firstValues to an integer
    firstValue = int(firstValues[index])
    # Convert the value at the current index in secondValues to an integer
    secondValue = int(secondValues[index])
    
    # Check if the values at the current index are different
    if firstValue != secondValue:
        # Increment the differenceCount by 1
        differenceCount += 1

# Check if differenceCount is less than 3
if differenceCount < 3:
    # Output "YES" if less than three values are different
    print("YES")
else:
    # Output "NO" if three or more values are different
    print("NO")

# End the main process
