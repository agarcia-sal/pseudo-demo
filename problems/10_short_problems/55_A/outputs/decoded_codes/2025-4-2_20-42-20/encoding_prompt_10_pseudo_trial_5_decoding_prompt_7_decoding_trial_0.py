# Initialize variable by reading user input and converting it to an integer
n = int(input())

# Create a list 'b' of Boolean values initialized to True with length 'n'
b = [True] * n

# Initialize counters
j = 0
i = 1

# Loop while 'i' is less than or equal to 500000
while i <= 500000:
    # Check if the current position 'j' is still True
    if b[j]:
        b[j] = False  # Mark the position as False

    # Increment 'i' and update 'j' for the next iteration
    i += 1
    j = (j + i) % n  # Update 'j' using modular arithmetic

# Create list 'x' to store positions in 'b' that are still True
x = [index for index, value in enumerate(b) if value]  # Get indices of True values in 'b'

# Check the length of 'x'
if len(x) == 0:  # If 'x' is empty
    print('YES')  # All values have been marked False
else:
    print('NO')  # There are still True values in 'b'
