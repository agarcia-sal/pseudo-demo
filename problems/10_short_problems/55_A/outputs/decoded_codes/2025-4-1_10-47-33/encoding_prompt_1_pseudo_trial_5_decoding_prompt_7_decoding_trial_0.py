# Step 1: Input the integer value representing the number of elements (n)
n = int(input())

# Step 2: Initialize a list (b) of size n with all values set to True
b = [True] * n

# Step 3: Set index variable j to 0
j = 0

# Step 4: Set counter variable i to 1
i = 1

# Step 5: While i is less than or equal to 500000, do the following
while i <= 500000:
    # Step 5a: If the value at index j in list b is True
    if b[j]:
        # Set the value at index j in list b to False
        b[j] = False
    
    # Step 5b: Increment the counter variable i by 1
    i += 1
    
    # Step 5c: Update the index j
    j = (j + i) % n

# Step 6: Create a new list (x) that contains all values from list b that are still True
x = [value for value in b if value]

# Step 7: If the length of list x is equal to 0
if len(x) == 0:
    # Step 7a: Output "YES"
    print("YES")
else:
    # Step 8: Otherwise, output "NO"
    print("NO")
