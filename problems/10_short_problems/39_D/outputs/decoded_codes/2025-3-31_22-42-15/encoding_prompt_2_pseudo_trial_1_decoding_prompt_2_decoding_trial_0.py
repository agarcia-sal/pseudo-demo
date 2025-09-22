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

# For each index from 0 to 2 (inclusive)
for index in range(3):
    # Convert the value at the current index in firstValues to an integer
    firstValue = int(firstValues[index])
    # Convert the value at the current index in secondValues to an integer
    secondValue = int(secondValues[index])
    # If firstValue is not equal to secondValue
    if firstValue != secondValue:
        # Increment the differenceCount by 1
        differenceCount += 1

# After comparing all three values, check if differenceCount is less than 3
if differenceCount < 3:
    # If it is, output "YES"
    print("YES")
else:
    # Otherwise, output "NO"
    print("NO")

# End the main process
