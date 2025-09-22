# Start
n = int(input())  # Step 2: Input an integer value n
b = [True] * n    # Step 3: Initialize list b with True values
j = 0             # Step 4: Initialize j to 0
i = 1             # Step 4: Initialize i to 1

# Step 5: Loop while i is less than or equal to 500,000
while i <= 500000:
    # Step 5.1: Check Condition
    if b[j]:  # If the value at position j in list b is True
        b[j] = False  # Step 5.1.1: Set position j in list b to False

    # Step 5.2: Increment i
    i += 1
    # Step 5.3: Update j
    j = (j + i) % n  # Wrap around using modulo n

# Step 6: Extract Result
x = [value for value in b if value]  # Create a list of all True values

# Step 7: Check Length
if len(x) == 0:  # If length of list x is zero
    print("YES")  # Step 7.1: Output "YES"
else:
    print("NO")   # Step 8: Output "NO"
# End
