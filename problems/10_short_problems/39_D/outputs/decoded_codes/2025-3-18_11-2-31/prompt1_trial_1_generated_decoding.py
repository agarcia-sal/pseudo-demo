# BEGIN Algorithm CheckDifferences

# Read the first input line and assign it to firstInput
firstInput = input()

# Read the second input line and assign it to secondInput
secondInput = input()

# Split the input lines into lists of strings
firstList = firstInput.split()
secondList = secondInput.split()

# Initialize counter for differences
differenceCount = 0

# Loop over the elements in the first three positions of both lists
for index in range(3):
    # Convert the string elements to integers
    firstValue = int(firstList[index])
    secondValue = int(secondList[index])

    # Check if the values are different
    if firstValue != secondValue:
        # Increment the difference counter
        differenceCount += 1

# If the count of differences is less than 3
if differenceCount < 3:
    # Output "YES"
    print("YES")
else:
    # Otherwise, output "NO"
    print("NO")

# END Algorithm CheckDifferences
