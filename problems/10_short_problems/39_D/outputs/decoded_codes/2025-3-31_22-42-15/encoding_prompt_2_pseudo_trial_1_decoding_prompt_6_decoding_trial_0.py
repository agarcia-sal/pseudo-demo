# Begin the main process

# Step 2: Prompt the user to input the first set of values and store it in first_input
first_input = input()

# Step 3: Prompt the user to input the second set of values and store it in second_input
second_input = input()

# Step 4: Split the first input string into a list of values and store it as first_values
first_values = first_input.split()

# Step 5: Split the second input string into a list of values and store it as second_values
second_values = second_input.split()

# Step 6: Initialize a counter variable called difference_count and set it to zero
difference_count = 0

# Step 7: For each index from 0 to 2 (inclusive)
for index in range(3):
    # Convert the value at the current index in first_values to an integer
    first_value = int(first_values[index])
    
    # Convert the value at the current index in second_values to an integer
    second_value = int(second_values[index])
    
    # If first_value is not equal to second_value, increment the difference_count by 1
    if first_value != second_value:
        difference_count += 1

# Step 8: After comparing all three values, check if difference_count is less than 3
if difference_count < 3:
    # If it is, output "YES"
    print("YES")
else:
    # Otherwise, output "NO"
    print("NO")

# End the main process
