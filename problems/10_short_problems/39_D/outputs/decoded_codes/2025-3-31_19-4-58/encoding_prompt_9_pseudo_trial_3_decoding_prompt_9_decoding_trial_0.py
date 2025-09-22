# Start Main Program

# Prompt the user for the first set of integers
firstSet = input()

# Prompt the user for the second set of integers
secondSet = input()

# Split input strings into lists
firstList = firstSet.split()
secondList = secondSet.split()

# Initialize difference counter
differenceCount = 0

# Check each position for differences
for index in range(3):  # Since we are looking at three positions (0, 1, 2)
    firstValue = int(firstList[index])      # Convert the element at index of firstList to integer
    secondValue = int(secondList[index])    # Convert the element at index of secondList to integer
    
    # If the values differ, increment the difference counter
    if firstValue != secondValue:
        differenceCount += 1

# Evaluate number of differences
if differenceCount < 3:
    print("YES")  # Output "YES" if differences are less than 3
else:
    print("NO")   # Output "NO" if differences are 3 or more 

# End Program
