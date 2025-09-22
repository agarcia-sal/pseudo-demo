# Start the main process

# Obtain the first set of input values from the user
firstInput = input()

# Obtain the second set of input values from the user
secondInput = input()

# Split firstInput into a list of values
firstValues = firstInput.split()

# Split secondInput into a list of values
secondValues = secondInput.split()

# Initialize discrepancyCount to keep track of the number of differences
discrepancyCount = 0

# Loop through the first three indices
for index in range(3):
    # Convert the value at the current index in firstValues to an integer
    valueFromFirst = int(firstValues[index])
    # Convert the value at the current index in secondValues to an integer
    valueFromSecond = int(secondValues[index])
    
    # Compare the two values
    if valueFromFirst != valueFromSecond:
        # If they are not equal, increment the discrepancy count
        discrepancyCount += 1

# Evaluate the discrepancyCount
if discrepancyCount < 3:
    # If less than 3 discrepancies, output "YES"
    print("YES")
else:
    # Otherwise, output "NO"
    print("NO")

# End the main process
