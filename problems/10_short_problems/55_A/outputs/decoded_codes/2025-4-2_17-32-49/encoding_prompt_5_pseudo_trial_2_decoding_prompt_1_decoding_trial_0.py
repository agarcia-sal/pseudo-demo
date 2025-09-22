# Step 1: Initialize Variables
n = int(input())  # Read an integer value `n` from user input
b = [True] * n    # Create list `b` of size `n`, initialized with all values set to True
j = 0              # Set index `j` to 0
i = 1              # Set index `i` to 1

# Step 2: Process the List
while i <= 500000:  # While i is less than or equal to 500000
    if b[j]:  # Check if the value at index `j` in list `b` is True
        b[j] = False  # If it is True, set b[j] to False
    i += 1  # Increment the value of `i` by 1
    j = (j + i) % n  # Update index `j` to a new position using (j + i) modulo n

# Step 3: Determine Remaining Values
x = [value for value in b if value]  # Create a new list `x` of remaining True values
if len(x) == 0:  # If the length of list `x` is 0
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"
