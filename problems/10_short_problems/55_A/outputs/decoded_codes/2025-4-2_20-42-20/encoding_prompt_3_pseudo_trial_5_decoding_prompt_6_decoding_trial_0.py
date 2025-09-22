# Step 1: Read an integer input representing the size of the list.
number_of_elements = int(input())  # Get the size of the boolean list from user input

# Step 2: Initialize a list with boolean values set to True.
boolean_list = [True] * number_of_elements  # Create a list filled with True values

# Step 3: Initialize variables for counting and indexing.
index = 0  # Start index at 0
increment = 1  # Start increment at 1

# Step 4: Iterate while increment is less than or equal to 500,000.
while increment <= 500000:
    # Step 5: Check if the current index in booleanList is True.
    if boolean_list[index]:  # If the value at the current index is True
        # Step 6: If True, set the current index in booleanList to False.
        boolean_list[index] = False  # Mark the current index as False

    # Step 7: Increment the value of increment.
    increment += 1  # Increase the increment by 1

    # Step 8: Update index using the formula to wrap around the list.
    index = (index + increment) % number_of_elements  # Calculate the new index

# Step 9: Create a new list of elements from boolean_list that are still True.
active_elements_list = [value for value in boolean_list if value]  # Filter the True values

# Step 10: Check if there are any True elements in the active_elements_list.
if len(active_elements_list) == 0:  # If no True elements remain
    # If no True elements remain, output 'YES'.
    print('YES')
else:
    # Otherwise, output 'NO'.
    print('NO')
