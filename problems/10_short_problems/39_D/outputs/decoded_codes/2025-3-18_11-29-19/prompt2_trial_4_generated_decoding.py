# Start the process

# Receive input
firstInput = input()
secondInput = input()

# Split the inputs into lists
firstList = firstInput.split()
secondList = secondInput.split()

# Initialize a counter for differences
differenceCount = 0

# Loop through the first three elements
for index in range(3):  # Loop through indices 0, 1, 2
    firstValue = int(firstList[index])       # Convert firstList element to integer
    secondValue = int(secondList[index])     # Convert secondList element to integer
    if firstValue != secondValue:             # Check for differences
        differenceCount += 1                   # Increase the counter for differences

# Check results
if differenceCount < 3:
    print("YES")                              # Print "YES" if differences are less than 3
else:
    print("NO")                               # Print "NO" otherwise

# End the process
