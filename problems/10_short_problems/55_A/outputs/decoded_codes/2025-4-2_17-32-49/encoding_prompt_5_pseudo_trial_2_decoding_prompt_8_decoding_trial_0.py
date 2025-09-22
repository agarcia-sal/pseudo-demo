# Initialize Variables
n = int(input())
b = [True] * n
j = 0
i = 1

# Process the List
while i <= 500000:
    if b[j]:  # Check if value at index j is TRUE
        b[j] = False  # Mark as visited
    i += 1  # Increment the iteration count
    j = (j + i) % n  # Update index j using modulo

# Determine Remaining Values
x = [value for value in b if value]  # List of all TRUE values remaining

# Output result
if len(x) == 0:
    print("YES")
else:
    print("NO")
