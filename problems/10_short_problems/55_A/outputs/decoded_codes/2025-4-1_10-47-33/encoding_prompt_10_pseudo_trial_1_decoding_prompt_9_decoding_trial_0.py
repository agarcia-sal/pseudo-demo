# Start Program

# Input: Set n to the integer value read from user input.
n = int(input())

# Initialize Boolean Array: Create a list b of size n, where each element is initialized to True.
b = [True] * n

# Initialize Counters: Set j to 0 (represents the current index in the array) and i to 1.
j = 0
i = 1

# Loop Until Limit: While i is less than or equal to 500,000
while i <= 500000:
    # Check Boolean Condition: If b[j] is True
    if b[j]:
        # Set b[j] to False (mark index j as processed).
        b[j] = False
    # Increment i by 1.
    i += 1
    # Update j to (j + i) mod n (calculate the next index in a circular manner).
    j = (j + i) % n

# Filter True Values: Create a list x composed of elements from b that are still True.
x = [value for value in b if value]

# Output Result: If the length of x is equal to 0
if len(x) == 0:
    print("YES")
else:
    print("NO")

# End Program
