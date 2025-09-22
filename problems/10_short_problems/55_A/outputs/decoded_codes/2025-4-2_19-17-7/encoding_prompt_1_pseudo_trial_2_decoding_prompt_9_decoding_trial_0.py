# Begin Process

# Step 2: Input
n = int(input())  # Read an integer value n from the user

# Step 3: Initialize
isActive = [True] * n  # Create a list of size n with all elements set to True
currentIndex = 0  # Set current index to 0
increment = 1  # Set increment to 1

# Step 4: Loop: while incrementing increment up to 500,000
while increment <= 500000:
    if isActive[currentIndex]:  # Check if currentIndex is active
        isActive[currentIndex] = False  # Set the current index as inactive

    increment += 1  # Increment the increment value
    currentIndex = (currentIndex + increment) % n  # Update currentIndex with wrap-around

# Step 5: Check for Active Elements
activeElements = [active for active in isActive if active]  # List of all active (True) elements

# Step 6: Output
if len(activeElements) == 0:  # If no active elements
    print('YES')  # Print 'YES'
else:
    print('NO')  # Otherwise, print 'NO'

# End Process
