# Begin the main program
n = int(input())  # Input the value of n
array_b = [True] * n  # Create an array b of size n and initialize all elements to True
index_j = 0  # Initialize index j
counter_i = 1  # Initialize counter i

# Loop until counter_i exceeds 500000
while counter_i <= 500000:
    if array_b[index_j]:  # Check if b[j] is True
        array_b[index_j] = False  # Mark the current position as False
    counter_i += 1  # Increment the counter to move to the next one
    index_j = (index_j + counter_i) % n  # Update index j based on current i

# Collect all True values from array_b
true_values = [value for value in array_b if value]

# Check if there are any True values left in true_values
if len(true_values) == 0:
    print('YES')  # All positions marked False
else:
    print('NO')   # There are still some True positions left
# End of the program
