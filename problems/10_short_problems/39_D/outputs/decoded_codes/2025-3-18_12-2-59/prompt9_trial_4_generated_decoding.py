# Start the main process
# Read the first set of integers from input
firstSet = input().split()
# Read the second set of integers from input
secondSet = input().split()

# Initialize a counter for differences
differenceCount = 0

# Compare corresponding integers
for index in range(3):  # Loop through each index from 0 to 2
    firstValue = int(firstSet[index])  # Convert firstSet value to integer
    secondValue = int(secondSet[index])  # Convert secondSet value to integer

    # If the values are not equal, increment the difference count
    if firstValue != secondValue:
        differenceCount += 1

# Evaluate the result
if differenceCount < 3:  # If differences are fewer than 3
    print("YES")
else:  # Otherwise, print "NO"
    print("NO")
