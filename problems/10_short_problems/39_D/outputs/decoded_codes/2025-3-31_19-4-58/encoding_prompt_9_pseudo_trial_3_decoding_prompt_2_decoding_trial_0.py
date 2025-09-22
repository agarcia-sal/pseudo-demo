# Start Main Program

# Prompt the user for the first set of integers and store it in a variable named `firstSet`
firstSet = input()

# Prompt the user for the second set of integers and store it in a variable named `secondSet`
secondSet = input()

# Split Input Strings
# Split `firstSet` into a list of strings named `firstList`
firstList = firstSet.split()

# Split `secondSet` into a list of strings named `secondList`
secondList = secondSet.split()

# Initialize Difference Counter
# Set a variable `differenceCount` to 0 to keep track of how many positions the sets differ.
differenceCount = 0

# Check Each Position for Differences
# For each index from 0 to 2 (representing the three positions), do the following:
for i in range(3):
    # Convert the element at that index of `firstList` to an integer
    firstValue = int(firstList[i])
    
    # Convert the element at that index of `secondList` to an integer
    secondValue = int(secondList[i])
    
    # If `firstValue` is not equal to `secondValue`, increment `differenceCount` by 1
    if firstValue != secondValue:
        differenceCount += 1

# Evaluate Number of Differences
# If `differenceCount` is less than 3, display "YES"
if differenceCount < 3:
    print("YES")
# Otherwise, display "NO"
else:
    print("NO")

# End Program
