# Step 1: Input Handling
n = int(input())  # Read an integer input for the size of the boolean list

# Step 2: Initialize a boolean list b
boolean_list = [True] * n  # Create a list of boolean values initialized to True
j = 0  # Initialize index j
i = 1  # Initialize index i

# Step 3: Loop to modify the boolean list
while i <= 500000:  # Loop until i reaches 500000
    if boolean_list[j]:  # If the current index in the list is True
        boolean_list[j] = False  # Set the value at this index to False

    # Step 4: Increment i and update j
    i += 1  # Increment i by 1
    j = (j + i) % n  # Update j using modulo to wrap around

# Step 5: Extract remaining TRUE values from boolean_list
remaining_true_values = [value for value in boolean_list if value]  # Filter the list for True values

# Step 6: Check the result and print output
if len(remaining_true_values) == 0:  # Check if the list of remaining True values is empty
    print('YES')  # Print 'YES' if there are no True values left
else:
    print('NO')  # Print 'NO' if there are still True values
