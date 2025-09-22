# Start of the program

# Step 1: Read an integer input representing the size of the array
size_of_array = int(input())

# Step 2: Initialize a boolean array where all elements are set to True
boolean_array = [True] * size_of_array

# Step 3: Set initial values for index variables
index_for_increment = 0
counter = 1

# Step 4: Iterate a maximum of 500,000 times
while counter <= 500000:
    # Step 5: If the current position in the boolean array is True
    if boolean_array[index_for_increment]:
        # Step 6: Mark the current position as False
        boolean_array[index_for_increment] = False

    # Step 7: Update the counter for the next iteration
    counter += 1
    
    # Step 8: Calculate the next index using modulo operation
    index_for_increment = (index_for_increment + counter) % size_of_array

# Step 9: Create a new list containing only True values from the boolean array
true_values_list = [value for value in boolean_array if value]

# Step 10: Check if the list of true values is empty
if len(true_values_list) == 0:
    # Print 'YES' if there are no true values remaining
    print('YES')
else:
    # Print 'NO' if there are still true values
    print('NO')

# End of the program
