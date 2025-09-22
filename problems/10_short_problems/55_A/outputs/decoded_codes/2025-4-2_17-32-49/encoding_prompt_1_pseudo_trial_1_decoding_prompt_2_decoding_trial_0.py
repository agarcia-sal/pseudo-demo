# Start

# Set up input
n = int(input())

# Initialize a list
isNotDeleted = [True] * n

# Set initial variables
currentIndex = 0
i = 1

# Loop through a range
while i <= 500000:
    if isNotDeleted[currentIndex]:
        isNotDeleted[currentIndex] = False  # mark as deleted
    i += 1
    currentIndex = (currentIndex + i) % n  # wrap around if needed

# Check for remaining True values
remainingTrue = [value for value in isNotDeleted if value]

# Determine output based on remaining values
if len(remainingTrue) == 0:
    print('YES')
else:
    print('NO')

# End
