# Begin the main program
n = int(input())  # Input the value of n
b = [True] * n  # Create an array b of size n and initialize all elements to True
j = 0  # Initialize index j
i = 1  # Initialize counter i

# Loop until i exceeds 500000
while i <= 500000:
    if b[j]:  # If b[j] is True
        b[j] = False  # Mark the current position as False
    i += 1  # Increment i by 1
    j = (j + i) % n  # Update index j based on current i

# Collect all True values from array b
x = [value for value in b if value]  # List of elements from b that are True

# Check if there are any True values left in x
if len(x) == 0:
    print('YES')  # All positions marked False
else:
    print('NO')   # There are still some True positions left
# End of the program
