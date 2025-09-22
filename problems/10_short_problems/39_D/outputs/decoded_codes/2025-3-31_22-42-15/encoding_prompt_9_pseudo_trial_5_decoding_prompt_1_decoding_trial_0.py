# 1. Start the main process.

# 2. Receive Input:
firstSet = input()  # Read the first line of input and store it as a string called firstSet.
secondSet = input()  # Read the second line of input and store it as a string called secondSet.

# 3. Split Input into Lists:
firstList = firstSet.split()  # Split firstSet into a list of strings called firstList.
secondList = secondSet.split()  # Split secondSet into a list of strings called secondList.

# 4. Initialize a Counter:
differenceCount = 0  # Set a variable called differenceCount to 0.

# 5. Compare Corresponding Values:
for index in range(3):  # For each position index from 0 to 2 (inclusive):
    valueFromFirst = int(firstList[index])  # Convert the value at index from firstList to an integer.
    valueFromSecond = int(secondList[index])  # Convert the value at index from secondList to an integer.
    if valueFromFirst != valueFromSecond:  # If valueFromFirst is not equal to valueFromSecond:
        differenceCount += 1  # Increment differenceCount by 1.

# 6. Evaluate the Result:
if differenceCount < 3:  # If differenceCount is less than 3:
    print("YES")  # Print "YES".
else:  # Otherwise:
    print("NO")  # Print "NO".

# 7. End the main process.
