# Begin the main process

# Obtain the first set of input values from the user
firstInput = input()

# Obtain the second set of input values from the user
secondInput = input()

# Split firstInput into a list of values
firstValues = firstInput.split()

# Split secondInput into a list of values
secondValues = secondInput.split()

# Initialize the discrepancy count to zero
discrepancyCount = 0

# For each index from 0 to 2
for i in range(3):
    # Convert the value at current index in firstValues to integer
    valueFromFirst = int(firstValues[i])
    
    # Convert the value at current index in secondValues to integer
    valueFromSecond = int(secondValues[i])
    
    # Compare the two values
    if valueFromFirst != valueFromSecond:
        # Increment discrepancyCount by 1
        discrepancyCount += 1

# Evaluate discrepancyCount
if discrepancyCount < 3:
    # Output "YES"
    print("YES")
else:
    # Output "NO"
    print("NO")

# End the main process
