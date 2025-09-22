# Start of the Python code

# Input: Read an integer value 'n' from the user
n = int(input())

# Initialize a boolean list 'b' of size 'n' with all values set to True
b = [True] * n

# Initialize variables
j = 0  # This will act as an index for the list 'b'
i = 1  # This is a counter that will increment in the loop

# Loop to perform operations while 'i' is less than or equal to 500000
while i <= 500000:
    # Check if the current index 'j' in the list 'b' is True
    if b[j]:
        # Set the current index 'j' to False
        b[j] = False
    
    # Increment 'i' by 1
    i += 1
    
    # Update index 'j' by adding the current value of 'i', and taking modulo n
    j = (j + i) % n

# Filter the list 'b' to collect all elements that are still True
x = [value for value in b if value]

# Check if the filtered list 'x' is empty
if len(x) == 0:
    # Output 'YES' if the list 'x' is empty
    print('YES')
else:
    # Output 'NO' if the list 'x' is not empty
    print('NO')

# End of the Python code
