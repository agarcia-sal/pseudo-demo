# Start of the program

# Step 2: Read an integer value n which represents the number of elements
n = int(input())

# Step 3: Initialize a list b of size n, filled with True values
b = [True] * n

# Step 4: Initialize j to 0 and i to 1
j = 0
i = 1

# Step 5: Loop while i is less than or equal to 500,000
while i <= 500_000:
    # Step 5.1: Check if the value at position j in list b is True
    if b[j]:
        # Step 5.1.1: Mark this position as False
        b[j] = False
        
    # Step 5.2: Increment the value of i by 1
    i += 1
    
    # Step 5.3: Update j to (j + i) modulo n
    j = (j + i) % n

# Step 6: Extract result: Create a new list x consisting of all True values from list b
x = [value for value in b if value]

# Step 7: Check if the length of list x is zero
if len(x) == 0:
    # Step 7.1: Output "YES" if all positions were marked
    print("YES")
else:
    # Step 8: Output "NO" otherwise
    print("NO")

# End of the program
