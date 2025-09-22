# Read an integer input
n = int(input())

# Initialize a boolean list of size n, all set to True
booleanList = [True] * n

# Variables to keep track of indices
j = 0
i = 1

# Loop until i exceeds 500000
while i <= 500000:
    # If the current position is True
    if booleanList[j]:
        # Set current position to False
        booleanList[j] = False

    # Increment i
    i += 1
    
    # Update j using wrap-around logic
    j = (j + i) % n

# Create a list of True values from booleanList
trueValuesList = [value for value in booleanList if value]

# Check if there are any True values left
if len(trueValuesList) == 0:
    # If no True values, print 'YES'
    print('YES')
else:
    # If there are True values, print 'NO'
    print('NO')
