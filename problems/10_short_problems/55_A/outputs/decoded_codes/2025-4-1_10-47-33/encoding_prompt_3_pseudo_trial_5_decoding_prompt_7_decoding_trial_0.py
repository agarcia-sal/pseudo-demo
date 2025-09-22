# Start of the implementation

# Step 1: Read an integer value 'n' from the user input
n = int(input())

# Step 2: Initialize a boolean list 'b' of size 'n' with all values set to True
b = [True] * n

# Step 3: Initialize variables
j = 0  # This will act as an index for the list 'b'
i = 1  # This is a counter that will increment in the loop

# Step 4: Loop to perform operations while 'i' is less than or equal to 500000
while i <= 500000:
    # Step 5: Check if the current index 'j' in the list 'b' is True
    if b[j]:
        # Step 6: Set the current index 'j' to False
        b[j] = False
    
    # Step 7: Increment 'i' by 1
    i += 1
    
    # Step 8: Update index 'j' by adding the current value of 'i', and taking modulo n
    j = (j + i) % n

# Step 9: Filter the list 'b' to collect all elements that are still True
# Create a new list 'x' containing all elements from 'b' that are True
x = [value for value in b if value]

# Step 10: Check if the filtered list 'x' is empty
if len(x) == 0:
    # Step 11: Output 'YES' if list 'x' is empty
    print('YES')
else:
    # Step 12: Output 'NO' if list 'x' is not empty
    print('NO')

# End of implementation
