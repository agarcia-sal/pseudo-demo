# Start the main process.

# Receive Input:
firstSet = input()
secondSet = input()

# Split Input into Lists:
firstList = firstSet.split()
secondList = secondSet.split()

# Initialize a Counter:
differenceCount = 0

# Compare Corresponding Values:
for index in range(3):
    valueFromFirst = int(firstList[index])
    valueFromSecond = int(secondList[index])
    if valueFromFirst != valueFromSecond:
        differenceCount += 1

# Evaluate the Result:
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End the main process.


   def compare_sets(set1, set2):
       # logic to compare sets
   