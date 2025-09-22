# Start the program.

# Prompt the user for input
user_input_1 = input()  # Get the first set of values from the user
user_input_2 = input()  # Get the second set of values from the user

# Split the input strings into individual components
value_list_1 = user_input_1.split()  # Break userInput1 into a list of values
value_list_2 = user_input_2.split()  # Break userInput2 into a list of values

# Initialize a counter for differences
difference_counter = 0  # Set differenceCounter to zero

# Compare the corresponding values from both lists
for index in range(3):  # Loop from index 0 to 2 (inclusive)
    # Convert the values to integer
    value_a = int(value_list_1[index])  # Get value from valueList1
    value_b = int(value_list_2[index])  # Get value from valueList2
    
    # Check if the values are not equal
    if value_a != value_b:
        difference_counter += 1  # Increment the counter if values differ

# Evaluate the total differences
if difference_counter < 3:
    print("YES")  # Output if differences are less than 3
else:
    print("NO")  # Output if differences are 3 or more

# End the program.
