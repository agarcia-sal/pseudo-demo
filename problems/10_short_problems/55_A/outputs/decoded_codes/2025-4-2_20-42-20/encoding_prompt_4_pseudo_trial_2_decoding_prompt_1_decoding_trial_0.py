# START

# Read an integer input for n
n = int(input())

# Initialize a boolean list of size n with all values set to True
b = [True] * n

# Initialize two variables j and i
j = 0
i = 1

# Loop until i exceeds 500000
while i <= 500000:
    # If the current element in list b at index j is True
    if b[j] == True:
        # Change the value at index j to False
        b[j] = False

    # Increment i by 1
    i += 1

    # Update j to the next index using modular arithmetic
    j = (j + i) % n

# Create a new list x containing all elements from b that are still True
x = [val for val in b if val]

# Check if there are no True values left in x
if len(x) == 0:
    print('YES')  # All positions were marked False
else:
    print('NO')   # There are still True positions left

# END
