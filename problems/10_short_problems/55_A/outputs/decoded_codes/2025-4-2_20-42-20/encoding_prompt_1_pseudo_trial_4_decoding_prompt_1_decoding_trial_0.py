# Start
# Input: Read an integer value n which represents the number of elements
n = int(input())  # Read an integer from input

# Initialize: Create a list b of size n, filled with True values
b = [True] * n  # List containing n elements, all set to True

# Initialize: Set j to 0 and i to 1
j = 0
i = 1

# Loop: While i is less than or equal to 500,000
while i <= 500000:
    # Check Condition: If the value at position j in list b is True
    if b[j]:
        # Set the value at position j in list b to False, marking it
        b[j] = False
    
    # Increment: Increase the value of i by 1
    i += 1
    
    # Update j: Set j to the value of (j + i) modulo n
    j = (j + i) % n

# Extract Result: Create a new list x consisting of all True values from list b
x = [value for value in b if value]

# Check Length: If the length of list x is zero
if len(x) == 0:
    # Output: Print "YES"
    print("YES")
else:
    # Output: Print "NO"
    print("NO")
# End
