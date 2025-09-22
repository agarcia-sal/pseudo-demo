# Start the program

# Step 2: Get an integer input called num
num = int(input())

# Step 3: Create a list called boolean_list initialized with True values of size num
boolean_list = [True] * num

# Step 4: Initialize an index variable called curr to 0
curr = 0

# Step 5: Initialize a step variable called step to 1
step = 1

# Step 6: While step is less than or equal to 500000
while step <= 500000:
    # a. If the value at boolean_list[curr] is True
    if boolean_list[curr]:
        # i. Set boolean_list[curr] to False  // Mark this index as processed
        boolean_list[curr] = False
    
    # b. Increment step by 1
    step += 1
    
    # c. Update curr as (curr + step) % num  // Move to the next index using modulo to wrap around
    curr = (curr + step) % num

# Step 7: Create a new list called rem containing all values in boolean_list that are still True
rem = [value for value in boolean_list if value]

# Step 8: If the size of rem is zero
if len(rem) == 0:
    # a. Output 'YES'  // All indices have been marked
    print('YES')
# Step 9: Else
else:
    # a. Output 'NO'  // Some indices are still unmarked
    print('NO')

# Step 10: End the program
