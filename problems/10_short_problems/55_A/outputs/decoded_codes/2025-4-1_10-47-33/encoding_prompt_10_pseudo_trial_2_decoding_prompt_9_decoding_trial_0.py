# Input integer value n
n = int(input())

# Step 2: Initialize a list of boolean values
b = [True] * n

# Step 3: Initialize variables
j = 0
i = 1

# Step 4: Loop until i exceeds 500000
while i <= 500000:
    # Step 5: Check if the current index in b is TRUE
    if b[j]:
        # Step 6: Set the current index to FALSE
        b[j] = False
    
    # Step 7: Increment i
    i += 1
    
    # Step 8: Update j to the next index in a circular manner
    j = (j + i) % n

# Step 9: Create a list x containing all TRUE values in b
x = [value for value in b if value]

# Step 10: Check if there are no TRUE values in x
if len(x) == 0:
    # Step 11: Print 'YES' if no TRUE values exist
    print('YES')
else:
    # Step 12: Print 'NO' if TRUE values exist
    print('NO')
