# Step 1: Get user input for the size of the list
size_of_list = int(input())  # n

# Step 2: Create a list of size n initialized with True values
boolean_list = [True] * size_of_list  # b

# Step 3: Initialize variables
index = 0  # j
i = 1      # i

# Step 4: Perform the operations as outlined in the pseudocode
while i <= 500000:  # While i is less than or equal to 500000
    if boolean_list[index]:  # If the current index is True
        boolean_list[index] = False  # Mark current index as False
    i += 1  # Increment i by 1
    index = (index + i) % size_of_list  # Update index with modulo operation

# Step 5: Create a list of all values from boolean_list that are True
true_values_list = [value for value in boolean_list if value]  # x

# Step 6: Check the length of the list containing True values
if len(true_values_list) == 0:  # If length of x is equal to 0
    print('YES')  # Print 'YES' if all elements were marked False
else:
    print('NO')   # Print 'NO' if there are still True elements in the list
