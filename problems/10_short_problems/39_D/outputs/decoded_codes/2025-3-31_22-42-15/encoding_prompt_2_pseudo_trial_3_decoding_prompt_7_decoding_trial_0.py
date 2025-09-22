# Begin the main process

# Step 2: Obtain the first set of input values from the user
firstInput = input() 

# Step 3: Obtain the second set of input values from the user
secondInput = input()

# Step 4: Split firstInput into a list of values
firstValues = firstInput.split() 

# Step 5: Split secondInput into a list of values
secondValues = secondInput.split() 

# Step 6: Initialize discrepancyCount to zero
discrepancyCount = 0

# Step 7: Loop through the first three indexes to check values
for index in range(3):  # Looping from index 0 to 2
    # Convert the current value in both lists to integers
    valueFromFirst = int(firstValues[index])  
    valueFromSecond = int(secondValues[index])  
    
    # Step 7: Compare the two values
    if valueFromFirst != valueFromSecond:  # If they are not equal
        discrepancyCount += 1  # Increment the discrepancy count

# Step 8: Evaluate the discrepancy count and output the result
if discrepancyCount < 3:  # If discrepancies are less than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"

# End the main process
