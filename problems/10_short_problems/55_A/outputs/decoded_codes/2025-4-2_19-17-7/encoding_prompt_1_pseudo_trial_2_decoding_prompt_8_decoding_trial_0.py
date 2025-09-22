# Begin Process

# Input
n = int(input())

# Initialize
isActive = [True] * n
currentIndex = 0
increment = 1

# Loop: while incrementing increment up to 500,000
while increment <= 500000:
    if isActive[currentIndex]:
        isActive[currentIndex] = False

    increment += 1
    currentIndex = (currentIndex + increment) % n  # Update using modular arithmetic

# Check for Active Elements
activeElements = [element for element in isActive if element]

# Output
if len(activeElements) == 0:
    print('YES')
else:
    print('NO')

# End Process
