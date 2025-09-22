# Start the main procedure

# Receive Input
firstInput = input()
secondInput = input()

# Process Input
firstValues = firstInput.split()
secondValues = secondInput.split()

# Initialize a count variable
discrepancyCount = 0  # This will keep track of the number of differences

# Comparison Loop
for index in range(3):  # Looping through the first three elements
    valueFromFirst = int(firstValues[index])  # Convert to integer
    valueFromSecond = int(secondValues[index])  # Convert to integer
    if valueFromFirst != valueFromSecond:  # Check for discrepancy
        discrepancyCount += 1  # Increment the count if they are not equal

# Final Decision
if discrepancyCount < 3:  # Check the count of discrepancies
    print("YES")  # Less than 3 discrepancies
else:
    print("NO")   # 3 or more discrepancies

# End the main procedure
