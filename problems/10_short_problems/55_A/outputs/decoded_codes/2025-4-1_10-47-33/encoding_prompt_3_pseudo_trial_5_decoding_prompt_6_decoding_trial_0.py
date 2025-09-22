# Start of Python Code

# Step 1: Input an integer value 'n' from the user
n = int(input())

# Step 2: Initialize a boolean list 'is_true_list' of size 'n' with all values set to True
is_true_list = [True] * n

# Step 3: Initialize variables
index = 0  # This will act as an index for the list 'is_true_list'
counter = 1  # This is a counter that will increment in the loop

# Step 4: Loop to perform operations while 'counter' is less than or equal to 500000
while counter <= 500000:
    # Step 5: Check if the current index 'index' in the list 'is_true_list' is True
    if is_true_list[index]:
        # Step 6: If it is True, set it to False
        is_true_list[index] = False
    
    # Step 7: Increment 'counter' by 1
    counter += 1

    # Step 8: Update index by adding the current value of 'counter', and taking modulo n
    index = (index + counter) % n

# Step 9: Filter the list 'is_true_list' to collect all elements that are still True
filtered_list = [value for value in is_true_list if value]

# Step 10: Check if the filtered list is empty
if len(filtered_list) == 0:
    # Output 'YES' if list is empty
    print('YES')
else:
    # Output 'NO' if list is not empty
    print('NO')

# End of Python Code
