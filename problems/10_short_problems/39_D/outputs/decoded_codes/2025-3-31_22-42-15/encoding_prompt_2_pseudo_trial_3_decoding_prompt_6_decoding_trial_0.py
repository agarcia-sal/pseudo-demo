# Begin the main process

# Step 2: Obtain the first set of input values and store in firstInput
first_input = input() 

# Step 3: Obtain the second set of input values and store in secondInput
second_input = input()

# Step 4: Split firstInput into a list of values
first_values = first_input.split()

# Step 5: Split secondInput into a list of values
second_values = second_input.split()

# Step 6: Initialize discrepancyCount to zero
discrepancy_count = 0

# Step 7: Check the first three values for discrepancies
for index in range(3):
    # Convert values to integers
    value_from_first = int(first_values[index])
    value_from_second = int(second_values[index])
    
    # Compare the two values
    if value_from_first != value_from_second:
        discrepancy_count += 1  # Increment discrepancyCount if not equal

# Step 8: Evaluate and output the result based on discrepancyCount
if discrepancy_count < 3:
    print("YES")
else:
    print("NO")

# End the main process
