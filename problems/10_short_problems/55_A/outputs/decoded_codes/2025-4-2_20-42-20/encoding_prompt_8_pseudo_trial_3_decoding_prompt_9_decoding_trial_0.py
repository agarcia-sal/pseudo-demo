# Get the total number of boolean elements from the user
n = int(input())

# Create a list of boolean values, all initialized to True
booleanList = [True] * n

# Initialize current position and increment for updates
currentIndex = 0
increment = 1
limit = 500000  # Setting a limit for the number of iterations

# Update loop
while increment <= limit:
    # Check if the current index in the boolean list is True
    if booleanList[currentIndex]:
        # Set the value at current index to False
        booleanList[currentIndex] = False
    
    # Update increment and currentIndex
    increment += 1
    currentIndex = (currentIndex + increment) % n  # Wrap around using modulo

# Create a list of remaining True values
remainingTrue = [value for value in booleanList if value]

# Output result based on the remaining True values
if len(remainingTrue) == 0:
    print('YES')
else:
    print('NO')
