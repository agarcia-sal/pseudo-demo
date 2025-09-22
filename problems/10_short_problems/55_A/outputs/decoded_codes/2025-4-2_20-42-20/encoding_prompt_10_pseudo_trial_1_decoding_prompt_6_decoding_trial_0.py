# Start of the program

# Step 2: Define an integer variable n
n = int(input())  # Step 3: Read input value and assign it to n

# Step 4: Create a list b of size n, initializing all elements to True
boolean_list = [True] * n  # List of boolean values initialized to True

# Step 5: Initialize integer variable j to 0
index_j = 0

# Step 6: Initialize integer variable i to 1
counter_i = 1

# Step 7: While counter_i is less than or equal to 500000 do:
while counter_i <= 500000:
    # Step 7a: If boolean_list[index_j] is True then:
    if boolean_list[index_j]:
        boolean_list[index_j] = False  # Step 7ai: Set to False
    
    counter_i += 1  # Step 7b: Increment counter_i by 1
    index_j = (index_j + counter_i) % n  # Step 7c: Update index_j

# Step 8: Create a new list x that contains all elements in boolean_list that are True
true_values_list = [value for value in boolean_list if value]

# Step 9: If the length of true_values_list is 0 then:
if len(true_values_list) == 0:
    print('YES')  # Step 9a: Print 'YES'
# Step 10: Else:
else:
    print('NO')   # Step 10a: Print 'NO'

# End of the program
