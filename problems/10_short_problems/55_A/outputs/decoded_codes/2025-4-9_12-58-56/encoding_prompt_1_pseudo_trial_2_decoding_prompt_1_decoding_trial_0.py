# Start the program

# Step 2: Get the number of elements (n) from user input and convert it to an integer.
n = int(input())

# Step 3: Initialize a boolean list (b) of size n, where each element is set to True.
b = [True] * n

# Step 4: Set initial variables for processing
j = 0  # used to track the current index
i = 1  # used to control the steps

# Step 5: Repeat while i is less than or equal to 500000
while i <= 500000:
    # Step 5.1: If the current element in list b at index j is True, set that element to False.
    if b[j]:
        b[j] = False
    
    # Step 5.2: Increase the primary step counter (i) by 1.
    i += 1

    # Step 5.3: Calculate the new index (j) using modulo to wrap around.
    j = (j + i) % n

# Step 6: Create a new list (x) that contains only the elements from b that are still True.
x = [value for value in b if value]

# Step 7: Check the length of the list x
# Step 7.1: If the length of x is zero, print 'YES'
if len(x) == 0:
    print('YES')
# Step 7.2: Otherwise, print 'NO'
else:
    print('NO')

# End the program
