# Step 1: Read input
n = int(input())

# Step 2: Create a boolean list of size n initialized to True
b = [True] * n

# Step 3: Initialize j and i
j = 0
i = 1

# Step 4: Begin WHILE loop
while i <= 500000:
    # IF condition
    if b[j]:
        # Mark current index as False
        b[j] = False
    
    # INCREMENT i by 1
    i += 1
    
    # Update index for the next iteration
    j = (j + i) % n

# Step 5: Create a list x containing all True values
x = [value for value in b if value]

# Step 6: Check the length of x and print results
if len(x) == 0:
    print('YES')  # All elements were marked False
else:
    print('NO')   # There are still True elements in the list
