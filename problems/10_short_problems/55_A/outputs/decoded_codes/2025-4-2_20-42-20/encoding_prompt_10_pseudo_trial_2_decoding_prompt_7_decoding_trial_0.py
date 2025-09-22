# Start the program
# Step 1: Input an integer n from the user
n = int(input())

# Step 2: Initialize an array b of size n with all values set to True
b = [True] * n

# Step 3: Initialize index j to 0 and step i to 1
j = 0
i = 1

# Step 4: Loop until i is less than or equal to 500000
while i <= 500000:
    # Step 4a: If b[j] is True, then set b[j] to False
    if b[j]:
        b[j] = False
    # Step 4b: Increment i by 1
    i += 1
    # Step 4c: Update j to (j + i) modulo n
    j = (j + i) % n

# Step 5: Create an array x to store elements from b that are still True
x = [value for value in b if value]

# Step 6: Check the size of x and output the appropriate message
if len(x) == 0:
    print("YES")
else:
    print("NO")
