# Step 1: Initialize the variable n from user input
n = int(input())

# Step 2: Create a list 'b' initialized to True for n elements
b = [True] * n

# Step 3: Initialize indices
j = 0
i = 1

# Step 4: Iterate while i is less than or equal to 500000
while i <= 500000:
    # If the current index in b is True
    if b[j] is True:
        # Set the current index in b to False
        b[j] = False
    
    # Increment i by 1
    i += 1
    
    # Update j to the next index, wrapping around using modulus n
    j = (j + i) % n

# Step 5: Create a list 'x' from b containing all elements that are still True
x = [value for value in b if value is True]

# Step 6: Check the length of list x
if len(x) == 0:
    # If x is empty, print 'YES'
    print('YES')
else:
    # Otherwise, print 'NO'
    print('NO')
