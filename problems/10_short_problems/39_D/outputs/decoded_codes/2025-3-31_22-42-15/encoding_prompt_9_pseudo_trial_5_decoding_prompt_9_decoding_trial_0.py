# Start the main process

# Receive Input:
firstSet = input()  # Read the first line of input
secondSet = input()  # Read the second line of input

# Split Input into Lists:
firstList = firstSet.split()  # Split firstSet into a list of strings
secondList = secondSet.split()  # Split secondSet into a list of strings

# Initialize a Counter:
differenceCount = 0  # This will track the number of positions where the values differ

# Compare Corresponding Values:
for index in range(3):  # Loop through index 0 to 2 (inclusive)
    valueFromFirst = int(firstList[index])  # Convert value at index from firstList to an integer
    valueFromSecond = int(secondList[index])  # Convert value at index from secondList to an integer
    if valueFromFirst != valueFromSecond:  # Check if they are not equal
        differenceCount += 1  # Increment differenceCount by 1

# Evaluate the Result:
if differenceCount < 3:  # If the count of differences is less than 3
    print("YES")  # Print "YES"
else:
    print("NO")  # Otherwise, print "NO"

# End the main process
