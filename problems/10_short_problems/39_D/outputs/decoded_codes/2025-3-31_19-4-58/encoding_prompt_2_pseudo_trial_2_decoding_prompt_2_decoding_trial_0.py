# Start the main procedure

# Receive Input
firstInput = input()
secondInput = input()

# Process Input
firstValues = firstInput.split()
secondValues = secondInput.split()

# Initialize a count variable
discrepancyCount = 0  # This will keep track of the number of differences between corresponding values

# Comparison Loop
for index in range(3):  # Loop through the first three elements
    valueFromFirst = int(firstValues[index])       # Convert the value at the current index in firstValues to an integer
    valueFromSecond = int(secondValues[index])     # Convert the value at the current index in secondValues to an integer
    
    # Check if valueFromFirst is not equal to valueFromSecond
    if valueFromFirst != valueFromSecond:
        discrepancyCount += 1  # Increment the discrepancyCount by 1 if they are not equal

# Final Decision
if discrepancyCount < 3:  # Check if discrepancyCount is less than 3
    print("YES")          # If it is less than 3, print "YES"
else:
    print("NO")           # Otherwise, print "NO"

# End the main procedure
