# Start the Program

# Receive Input
first_set = input()  # Enter first set of three numbers
second_set = input()  # Enter second set of three numbers

# Split Input into Individual Numbers
first_list = first_set.split()  # Split the first set into a list
second_list = second_set.split()  # Split the second set into a list

# Initialize a Counter for Differences
difference_count = 0  # Count of differing numbers

# Compare Each Number in the Sets
for index in range(3):  # Loop through indices 0 to 2
    first_number = int(first_list[index])  # Convert to integer
    second_number = int(second_list[index])  # Convert to integer
    if first_number != second_number:  # Check for difference
        difference_count += 1  # Increment the counter if they differ

# Determine the Result
if difference_count < 3:  # Check if differences are fewer than 3
    print("YES")  # Output YES if fewer than 3 different
else:
    print("NO")  # Output NO if 3 or more different

# End the Program
