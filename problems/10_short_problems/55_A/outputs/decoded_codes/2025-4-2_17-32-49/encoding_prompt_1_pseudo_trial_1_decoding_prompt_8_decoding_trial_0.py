# Start

# Step 1: Set up input
n = int(input())

# Step 2: Initialize a list
isNotDeleted = [True] * n

# Step 3: Set initial variables
currentIndex = 0
i = 1

# Step 4: Loop through a range
while i <= 500000:
    if isNotDeleted[currentIndex]:
        isNotDeleted[currentIndex] = False  # Mark as deleted
    i += 1
    currentIndex = (currentIndex + i) % n  # Wrap around if needed

# Step 5: Check for remaining True values
remainingTrue = [value for value in isNotDeleted if value]

# Step 6: Determine output based on remaining values
if len(remainingTrue) == 0:
    print('YES')
else:
    print('NO')

# End
