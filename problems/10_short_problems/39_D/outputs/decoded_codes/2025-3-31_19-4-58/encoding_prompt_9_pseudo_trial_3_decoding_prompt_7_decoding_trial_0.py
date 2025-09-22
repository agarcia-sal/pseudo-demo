# Start Main Program
# Prompt the user for the first set of integers
firstSet = input()
# Prompt the user for the second set of integers
secondSet = input()

# Split Input Strings
firstList = firstSet.split()  # Split the input string into a list of strings
secondList = secondSet.split()  # Split the second input string into a list of strings

# Initialize Difference Counter
differenceCount = 0  # Counter for the number of differing positions

# Check Each Position for Differences
for index in range(3):  # We are only interested in the first three positions (indices 0 to 2)
    firstValue = int(firstList[index])  # Convert the string at current index to an integer
    secondValue = int(secondList[index])  # Convert the corresponding string to an integer
    if firstValue != secondValue:  # If the values differ
        differenceCount += 1  # Increment the difference counter

# Evaluate Number of Differences
if differenceCount < 3:  # If differences are less than three
    print("YES")  # Output YES
else:
    print("NO")  # Output NO

# End Program
