# Start the main procedure

# Receive Input
firstInput = input()
secondInput = input()

# Process Input
firstValues = firstInput.split()
secondValues = secondInput.split()

# Initialize a count variable
discrepancyCount = 0

# Comparison Loop
for index in range(3):  # Looping through indices 0 to 2
    valueFromFirst = int(firstValues[index])  # Convert value from first input to integer
    valueFromSecond = int(secondValues[index])  # Convert value from second input to integer
    
    # Check if the values are not equal
    if valueFromFirst != valueFromSecond:
        discrepancyCount += 1  # Increment discrepancy count if they are not equal

# Final Decision
if discrepancyCount < 3:
    print("YES")  # Print YES if discrepancies are less than 3
else:
    print("NO")   # Print NO otherwise

# End the main procedure
