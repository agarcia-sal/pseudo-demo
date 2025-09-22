# Begin the main process

# Step 2: Obtain the first set of input values from the user
first_input = input()

# Step 3: Obtain the second set of input values from the user
second_input = input()

# Step 4: Split the first input into a list of values
first_values = first_input.split()

# Step 5: Split the second input into a list of values
second_values = second_input.split()

# Step 6: Initialize discrepancy count to zero
discrepancy_count = 0

# Step 7: For each index from 0 to 2 (first three values)
for index in range(3):
    # Convert values to integer
    value_from_first = int(first_values[index])
    value_from_second = int(second_values[index])
    
    # Compare the two values
    if value_from_first != value_from_second:
        discrepancy_count += 1

# Step 8: Evaluate discrepancy count
if discrepancy_count < 3:
    print("YES")
else:
    print("NO")

# End the main process
