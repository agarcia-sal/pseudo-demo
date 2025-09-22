# Read an integer input representing the size of the array
n = int(input())

# Create a boolean array initialized to True
booleanArray = [True] * n

# Initialize index j to 0
j = 0
# Initialize counter i to 1
i = 1

# Loop while counter i is less than or equal to 500000
while i <= 500000:
    # Check if the current index in booleanArray is True
    if booleanArray[j]:
        # Set the current index to False
        booleanArray[j] = False
    
    # Increment counter i
    i += 1
    
    # Update index j using circular indexing with the size of the array
    j = (j + i) % n

# Create a list x containing all True values from booleanArray
x = [value for value in booleanArray if value]

# Check the length of the list x
if len(x) == 0:
    print('YES')  # Output YES if no True values remain
else:
    print('NO')  # Output NO if some True values remain
