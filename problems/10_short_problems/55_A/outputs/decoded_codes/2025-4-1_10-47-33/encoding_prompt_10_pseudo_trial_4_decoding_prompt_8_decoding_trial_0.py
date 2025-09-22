# Step 1: Input Handling
n = int(input())

# Step 2: Initialize a boolean list b
b = [True] * n
j = 0
i = 1

# Step 3: Loop to modify the boolean list
while i <= 500000:
    if b[j]:
        b[j] = False
    
    # Step 4: Increment i and update j
    i += 1
    j = (j + i) % n

# Step 5: Extract remaining TRUE values from b
x = [value for value in b if value]

# Step 6: Check the result and print output
if len(x) == 0:
    print('YES')
else:
    print('NO')
