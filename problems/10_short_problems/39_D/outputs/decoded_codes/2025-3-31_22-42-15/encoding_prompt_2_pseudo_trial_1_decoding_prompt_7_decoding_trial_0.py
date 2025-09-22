# Begin the main process

# Prompt the user to input the first set of values and store it in firstInput
firstInput = input()

# Prompt the user to input the second set of values and store it in secondInput
secondInput = input()

# Split the first input string into a list of values and store it as firstValues
firstValues = firstInput.split()

# Split the second input string into a list of values and store it as secondValues
secondValues = secondInput.split()

# Initialize a counter variable called differenceCount and set it to zero
differenceCount = 0

# For each index from 0 to 2 (inclusive), compare the corresponding values
for index in range(3):
    # Convert the value at the current index in firstValues to an integer
    # and store it in firstValue
    firstValue = int(firstValues[index])
    
    # Convert the value at the current index in secondValues to an integer
    # and store it in secondValue
    secondValue = int(secondValues[index])
    
    # If firstValue is not equal to secondValue, increment differenceCount by 1
    if firstValue != secondValue:
        differenceCount += 1

# After comparing all three values, check if differenceCount is less than 3
if differenceCount < 3:
    # If it is, output "YES"
    print("YES")
else:
    # Otherwise, output "NO"
    print("NO")

# End the main process
