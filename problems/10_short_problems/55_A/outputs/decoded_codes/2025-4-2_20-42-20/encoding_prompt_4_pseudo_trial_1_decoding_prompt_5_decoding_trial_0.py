# Get the number of elements from user input
n = int(input())

# Create a list initialized with True values
b = [True] * n

# Initialize indices
j = 0
i = 1

# Loop until i is less than or equal to 500000
while i <= 500000:
    if b[j]:  # Check if current index is True
        b[j] = False  # Mark current index as False
    i += 1  # Increment i
    j = (j + i) % n  # Update index for the next iteration

# Create a list of all values from b that are still True
x = [value for value in b if value]

# Check if the length of x is zero and print the result
if len(x) == 0:
    print('YES')  # All elements were marked False
else:
    print('NO')   # There are still True elements in the list
