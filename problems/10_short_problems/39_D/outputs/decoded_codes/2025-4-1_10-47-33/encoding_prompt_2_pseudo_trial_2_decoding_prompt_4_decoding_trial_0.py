# Start the program.

# Receive input
first_input = input()
second_input = input()

# Process the inputs
first_list = first_input.split()
second_list = second_input.split()
difference_count = 0  # Initialize a variable to track differing elements

# Compare elements
for index in range(3):  # Loop through the first three indices
    first_number = int(first_list[index])  # Convert element to integer from firstList
    second_number = int(second_list[index])  # Convert element to integer from secondList
    
    if first_number != second_number:
        difference_count += 1  # Increment count if numbers are different

# Evaluate the results
if difference_count < 3:
    print("YES")
else:
    print("NO")

# End the program.
