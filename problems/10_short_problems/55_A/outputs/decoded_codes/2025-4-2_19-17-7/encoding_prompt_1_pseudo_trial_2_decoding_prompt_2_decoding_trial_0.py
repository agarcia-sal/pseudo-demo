# Begin Process

# Input: Read an integer value n from the user.
n = int(input())

# Initialize: Create a list isActive of size n with all elements set to True.
isActive = [True] * n
currentIndex = 0
increment = 1

# Loop: while incrementing increment up to 500,000
while increment <= 500000:
    # If the value at isActive[currentIndex] is True:
    if isActive[currentIndex]:
        # Set isActive[currentIndex] to False.
        isActive[currentIndex] = False
        
    # Increment increment by 1.
    increment += 1
    
    # Update currentIndex to be (currentIndex + increment) % n
    currentIndex = (currentIndex + increment) % n

# Check for Active Elements: Create a new list activeElements
activeElements = [x for x in isActive if x]

# Output: Check the length of activeElements
if len(activeElements) == 0:
    print('YES')
else:
    print('NO')

# End Process
