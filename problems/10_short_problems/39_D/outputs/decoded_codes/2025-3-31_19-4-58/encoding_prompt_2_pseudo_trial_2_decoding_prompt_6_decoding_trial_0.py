# Start the main procedure

# Step 2: Receive Input
first_input = input()  # Input for the first set of values
second_input = input()  # Input for the second set of values

# Step 3: Process Input
first_values = first_input.split()  # Split first input into a list
second_values = second_input.split()  # Split second input into a list

# Step 4: Initialize a count variable
discrepancy_count = 0  # This will keep track of differences

# Step 5: Comparison Loop
for index in range(3):  # Loop through the first three elements
    value_from_first = int(first_values[index])  # Convert to integer
    value_from_second = int(second_values[index])  # Convert to integer
    
    # Check for discrepancy
    if value_from_first != value_from_second:
        discrepancy_count += 1  # Increment count if they differ

# Step 6: Final Decision
if discrepancy_count < 3:
    print("YES")  # Print YES if discrepancies are less than 3
else:
    print("NO")  # Print NO otherwise

# End of the main procedure
