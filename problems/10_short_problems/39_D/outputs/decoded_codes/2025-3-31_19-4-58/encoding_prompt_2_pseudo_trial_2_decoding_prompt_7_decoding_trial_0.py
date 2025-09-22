# Start the main procedure

# Step 2: Receive Input
# Prompt the user to enter the first set of values
firstInput = input()
# Prompt the user to enter the second set of values
secondInput = input()

# Step 3: Process Input
# Split the inputs into individual components and store them in lists
firstValues = firstInput.split()
secondValues = secondInput.split()

# Step 4: Initialize a count variable
discrepancyCount = 0  # This will keep track of the number of differences between corresponding values

# Step 5: Comparison Loop
# For each index from 0 to 2 (representing the first three elements of the lists)
for index in range(3):
    # Convert the value at the current index in both lists to integers
    valueFromFirst = int(firstValues[index])
    valueFromSecond = int(secondValues[index])
    
    # Check if the values are not equal
    if valueFromFirst != valueFromSecond:
        discrepancyCount += 1  # Increment the discrepancy count if they are different

# Step 6: Final Decision
# After the loop, check if discrepancyCount is less than 3
if discrepancyCount < 3:
    print("YES")  # Print "YES" if discrepancies are less than 3
else:
    print("NO")   # Print "NO" if discrepancies are 3 or more

# End the main procedure
