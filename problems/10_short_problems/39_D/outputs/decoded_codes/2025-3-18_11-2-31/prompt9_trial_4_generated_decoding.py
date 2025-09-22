# Start the program.

# Receive Input Values
# Prompt the user to input the first set of three numbers (string format).
first_set_input = input()  # First set of numbers
# Prompt the user to input the second set of three numbers (string format).
second_set_input = input()  # Second set of numbers

# Split Input Strings into Lists
first_set = first_set_input.split()  # Convert the first input string into a list
second_set = second_set_input.split()  # Convert the second input string into a list

# Initialize a Counter for Differences
difference_counter = 0  # Set counter for differences

# Compare Values from Both Sets
for index in range(3):  # Loop through the indices 0 to 2
    first_value = int(first_set[index])  # Convert the first set value to an integer
    second_value = int(second_set[index])  # Convert the second set value to an integer
    if first_value != second_value:  # Compare the values
        difference_counter += 1  # Increment counter if values are different

# Evaluate the Results
if difference_counter < 3:  # If less than 3 differences exist
    print("YES")  # At least one value matches
else:
    print("NO")  # All values differ

# End the program.
