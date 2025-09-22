# Begin Process

# Input: Read an integer from the user
n = int(input())

# Initialize: Create a list of booleans, set to True; initialize currentIndex and increment
isActive = [True] * n  # A list of size n initialized to True
currentIndex = 0
increment = 1

# Loop: Increment up to 500,000
while increment <= 500000:
    # Check if the current index is active
    if isActive[currentIndex]:
        isActive[currentIndex] = False  # Set the current index to inactive (False)

    # Increment by 1
    increment += 1

    # Update currentIndex while ensuring it wraps around using modulo operation
    currentIndex = (currentIndex + increment) % n

# Check for Active Elements
activeElements = [x for x in isActive if x]  # Create a list of all True values

# Output: Determine if there are any active elements left
if len(activeElements) == 0:
    print('YES')  # If no active elements, print 'YES'
else:
    print('NO')   # If there are active elements, print 'NO'

# End Process
