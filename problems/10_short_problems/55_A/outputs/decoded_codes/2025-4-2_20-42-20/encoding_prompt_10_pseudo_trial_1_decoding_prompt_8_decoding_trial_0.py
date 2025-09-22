# Start

# Step 2: Define integer variable n
n = int(input())

# Step 4: Create a list b of size n, initializing all elements to True
b = [True] * n

# Step 5: Initialize integer variable j to 0
j = 0

# Step 6: Initialize integer variable i to 1
i = 1

# Step 7: While i is less than or equal to 500000 do:
while i <= 500000:
    # Step 7a: If b[j] is True then:
    if b[j]:
        # Step 7a.i: Set b[j] to False
        b[j] = False
        
    # Step 7b: Increment i by 1
    i += 1
    
    # Step 7c: Update j by calculating (j + i) modulo n
    j = (j + i) % n

# Step 8: Create a new list x that contains all elements in b that are True
x = [value for value in b if value]

# Step 9: If the length of x is 0 then:
if len(x) == 0:
    # Step 9a: Print 'YES'
    print('YES')
else:
    # Step 10a: Print 'NO'
    print('NO')

# End
